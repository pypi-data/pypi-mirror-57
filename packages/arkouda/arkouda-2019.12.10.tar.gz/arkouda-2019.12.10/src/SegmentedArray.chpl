module SegmentedArray {
  use MultiTypeSymbolTable;
  use MultiTypeSymEntry;
  use UnorderedCopy;
  use SipHash;
  use SegStringSort;
  use RadixSortLSD only radixSortLSD_ranks;
  use Reflection;
  use PrivateDist;
  use ServerConfig;
  use Time only getCurrentTime;

  private config const DEBUG = false;
  private config param useHash = false;
  param SegmentedArrayUseHash = useHash;
  
  class OutOfBoundsError: Error {}

  /* Represents an array of strings, implemented as a segmented array of bytes.
     Instances are ephemeral, not stored in the symbol table. Instead, attributes
     of this class refer to symbol table entries that persist. This class is a
     convenience for bundling those persistent objects and defining string-relevant
     operations.
   */
  class SegString {
    // Start indices of individual strings
    var offsets: borrowed SymEntry(int);
    // Bytes of all strings, joined by nulls
    var values: borrowed SymEntry(uint(8));
    // Number of strings
    var size: int;
    // Total number of bytes in all strings, including nulls
    var nBytes: int;

    /* This initializer is used when the SymEntries for offsets and values are
       already in the namespace. */
    proc init(segments: borrowed SymEntry(int), values: borrowed SymEntry(uint(8))) {
      offsets = segments;
      values = values;
      size = segments.size;
      nBytes = values.size;
    }

    /* This initializer is the most common, and is used when only the server
       names of the SymEntries are known. It handles the lookup. */
    proc init(segName: string, valName: string, st: borrowed SymTab) {
      // The try! is needed here because init cannot throw
      var gs = try! st.lookup(segName);
      // I want this to be borrowed, but that give a lifetime error
      var segs = toSymEntry(gs, int): unmanaged SymEntry(int);
      offsets = segs;
      var vs = try! st.lookup(valName);
      var vals = toSymEntry(vs, uint(8)): unmanaged SymEntry(uint(8));
      values = vals;
      size = segs.size;
      nBytes = vals.size;
    }

    /* Retrieve one string from the array */
    proc this(idx: int): string throws {
      if (idx < offsets.aD.low) || (idx > offsets.aD.high) {
        throw new owned OutOfBoundsError();
      }
      // Start index of the string
      var start = offsets.a[idx];
      // Index of last (null) byte in string
      var end: int;
      if (idx == size - 1) {
        end = nBytes - 1;
      } else {
        end = offsets.a[idx+1] - 1;
      }
      // Take the slice of the bytearray and "cast" it to a chpl string
      var s = interpretAsString(values.a[start..end]);
      return s;
    }

    /* Take a slice of strings from the array. The slice must be a 
       Chapel range, i.e. low..high by stride, not a Python slice.
       Returns arrays for the segment offsets and bytes of the slice.*/
    proc this(slice: range(stridable=true)) throws {
      if (slice.low < offsets.aD.low) || (slice.high > offsets.aD.high) {
        throw new owned OutOfBoundsError();
      }
      // Early return for zero-length result
      if (size == 0) || (slice.size == 0) {
        return (makeDistArray(0, int), makeDistArray(0, uint(8)));
      }
      // Start of bytearray slice
      var start = offsets.a[slice.low];
      // End of bytearray slice
      var end: int;
      if (slice.high == offsets.aD.high) {
        // if slice includes the last string, go to the end of values
        end = values.aD.high;
      } else {
        end = offsets.a[slice.high+1] - 1;
      }
      // Segment offsets of the new slice
      var newSegs = makeDistArray(slice.size, int);
      // Offsets need to be re-zeroed
      newSegs = offsets.a[slice] - start;
      // Bytearray of the new slice
      var newVals = makeDistArray(end - start + 1, uint(8));
      newVals = values.a[start..end];
      return (newSegs, newVals);
    }

    /* Gather strings by index. Returns arrays for the segment offsets
       and bytes of the gathered strings.*/
    proc this(iv: [?D] int) throws {
      // Early return for zero-length result
      if (D.size == 0) {
        return (makeDistArray(0, int), makeDistArray(0, uint(8)));
      }
      // Check all indices within bounds
      var ivMin = min reduce iv;
      var ivMax = max reduce iv;
      if (ivMin < 0) || (ivMax >= offsets.size) {
        throw new owned OutOfBoundsError();
      }
      if v {writeln("Computing lengths and offsets"); stdout.flush();}
      var t1 = getCurrentTime();
      ref oa = offsets.a;
      const low = offsets.aD.low, high = offsets.aD.high;
      // Lengths of segments including null bytes
      var gatheredLengths: [D] int;
      [(gl, idx) in zip(gatheredLengths, iv)] {
        var l: int;
        if (idx == high) {
          l = values.size - oa[high];
        } else {
          l = oa[idx+1] - oa[idx];
        }
        unorderedCopy(gl, l);
      }
      // The returned offsets are the 0-up cumulative lengths
      var gatheredOffsets = (+ scan gatheredLengths);
      // The total number of bytes in the gathered strings
      var retBytes = gatheredOffsets[D.high];
      gatheredOffsets -= gatheredLengths;
      if v {
        writeln(getCurrentTime() - t1, " seconds");
        writeln("Copying values"); stdout.flush();
        t1 = getCurrentTime();
      }
      var gatheredVals = makeDistArray(retBytes, uint(8));
      ref va = values.a;
      // Copy string data to gathered result
      forall (go, gl, idx) in zip(gatheredOffsets, gatheredLengths, iv) {
        for pos in 0..#gl {
          unorderedCopy(gatheredVals[go+pos], va[oa[idx]+pos]);
        }
      }
      if v {writeln(getCurrentTime() - t1, " seconds"); stdout.flush();}
      return (gatheredOffsets, gatheredVals);
    }

    /* Logical indexing (compress) of strings. */
    proc this(iv: [?D] bool) throws {
      // Index vector must be same domain as array
      if (D != offsets.aD) {
        throw new owned OutOfBoundsError();
      }
      if v {writeln("Computing lengths and offsets"); stdout.flush();}
      var t1 = getCurrentTime();
      ref oa = offsets.a;
      const low = offsets.aD.low, high = offsets.aD.high;
      // Calculate the destination indices
      var steps = + scan iv;
      var newSize = steps[high];
      // Early return for zero-length result
      if (newSize == 0) {
        return (makeDistArray(0, int), makeDistArray(0, uint(8)));
      }
      var segInds = makeDistArray(newSize, int);
      // Lengths of dest segments including null bytes
      var gatheredLengths = makeDistArray(newSize, int);
      forall (idx, present, i) in zip(D, iv, steps) {
        if present {
          segInds[i-1] = idx;
          if (idx == high) {
            gatheredLengths[i-1] = values.size - oa[high];
          } else {
            gatheredLengths[i-1] = oa[idx+1] - oa[idx];
          }
        }
      }
      // Make dest offsets from lengths
      var gatheredOffsets = (+ scan gatheredLengths);
      var retBytes = gatheredOffsets[newSize-1];
      gatheredOffsets -= gatheredLengths;
      if v {
        writeln(getCurrentTime() - t1, " seconds");
        writeln("Copying values"); stdout.flush();
        t1 = getCurrentTime();
      }
      var gatheredVals = makeDistArray(retBytes, uint(8));
      ref va = values.a;
      if DEBUG {
        printAry("gatheredOffsets: ", gatheredOffsets);
        printAry("gatheredLengths: ", gatheredLengths);
        printAry("segInds: ", segInds);
      }
      // Copy string bytes from src to dest
      forall (go, gl, idx) in zip(gatheredOffsets, gatheredLengths, segInds) {
        gatheredVals[{go..#gl}] = va[{oa[idx]..#gl}];
      }
      if v {writeln(getCurrentTime() - t1, " seconds"); stdout.flush();}
      return (gatheredOffsets, gatheredVals);
    }

    /* Apply a hash function to all strings. This is useful for grouping
       and set membership. The hash used is SipHash128.*/
    proc hash(const hashKey=defaultSipHashKey) throws {
      // 128-bit hash values represented as 2-tuples of uint(64)
      var hashes: [offsets.aD] 2*uint(64);
      // Early exit for zero-length result
      if (size == 0) {
        return hashes;
      }
      ref oa = offsets.a;
      ref va = values.a;
      if v {writeln("Computing segment lengths"); stdout.flush();}
      var t1 = getCurrentTime();
      // Compute lengths of strings
      var lengths = getLengths();
      if v {
        writeln(getCurrentTime() - t1, " seconds");
        writeln("Hashing strings"); stdout.flush();
        t1 = getCurrentTime();
      }      
      // Hash each string
      forall (o, l, h) in zip(oa, lengths, hashes) {
        // localize the string bytes
        const myBytes = va[{o..#l}];
        h = sipHash128(myBytes, hashKey);
        // Perf Note: localizing string bytes is ~3x faster on IB multilocale than this:
        // h = sipHash128(va[{o..#l}]);
      }
      if v {writeln(getCurrentTime() - t1, " seconds"); stdout.flush();}
      return hashes;
    }

    /* Return a permutation that groups the strings. Because hashing is used,
       this permutation will not sort the strings, but all equivalent strings
       will fall in one contiguous block. */
    proc argGroup() throws {
      if useHash {
        // Hash all strings
        var hashes = this.hash();
        // Return the permutation that sorts the hashes
        var iv = radixSortLSD_ranks(hashes);
        if DEBUG {
          var sortedHashes = [i in iv] hashes[i];
          var diffs = sortedHashes[(iv.domain.low+1)..#(iv.size-1)] - sortedHashes[(iv.domain.low)..#(iv.size-1)];
          printAry("diffs = ", diffs);
          var nonDecreasing = [d in diffs] ((d[1] > 0) || ((d[1] == 0) && (d[2] >= 0)));
          writeln("Are hashes sorted? ", && reduce nonDecreasing);
        }
        return iv;
      } else {
        var iv = argsort();
        return iv;
      }
    }

    proc getLengths() {
      var lengths: [offsets.aD] int;
      if (size == 0) {
        return lengths;
      }
      ref oa = offsets.a;
      const low = offsets.aD.low;
      const high = offsets.aD.high;
      lengths[low..high-1] = (oa[low+1..high] - oa[low..high-1]);
      lengths[high] = values.size - oa[high];
      /* forall (idx, l) in zip(offsets.aD, lengths) { */
      /*   if (idx == offsets.aD.high) { */
      /*     l = values.size - oa[idx]; */
      /*   } else { */
      /*     l = oa[idx+1] - oa[idx]; */
      /*   } */
      /* } */
      return lengths;
    }

    proc substringSearch(const substr: string, mode: SearchMode) throws {
      /* coforall loc in Locales { */
      /*   on loc { */
      /*     ref D = values.aD.localSubdomain(); */
      /*     coforall task in here.maxTaskPar { */
      /*       const mySubstr = substr.localize(); */
      /*       const mySize = (D.size / here.maxTaskPar) + if (task < (D.size % here.maxTaskPar)) then 1 else 0; */
      /*       const myStart = D.low + task * (D.size / here.maxTaskPar) + min(task, D.size % here.maxTaskPar); */
      /*       var subind = 1; */
      /*       for byte in values.localSlice[{myStart..#mySize}] { */
      /*         if (byte != mySubstr[subind]) { */
      /*           // No match; reset index */
      /*           subind = 1; */
      /*         } else { */
      /*           if (subind == mySubstr.numBytes) { */
      /*             // We have a match */
      /*             // Lookup segment */
                  
      /*           } else { */
      /*             // Still a candidate, but not yet a match */
      /*             subind += 1; */
      /*           } */
      /*         } */
      /*       } */
      /*     } */
      /*   } */
      /* } */
      var truth: [offsets.aD] bool;
      if (size == 0) || (substr.size == 0) {
        return truth;
      }
      var lengths = getLengths() - 1;
      ref oa = offsets.a;
      ref va = values.a;
      var locSubstr: [PrivateSpace] string;
      coforall loc in Locales {
        locSubstr[here.id] = substr.localize();
      }
      forall (o, l, t) in zip(oa, lengths, truth) {
        // Only compare if segment is long enough to contain substr
        if (locSubstr[here.id].numBytes <= l) {
          // Execute where the bytes are
          on va[o] {
            const ref mySub = locSubstr[here.id];
            const ref myVal = va[{o..#l}];
            var res: bool;
            select mode {
              when SearchMode.contains {
                res = segmentContains(myVal, mySub);
              }
              when SearchMode.startsWith {
                res = segmentStartsWith(myVal, mySub);
              }
              when SearchMode.endsWith {
                res = segmentEndsWith(myVal, mySub);
              }
              otherwise { throw new owned UnknownSearchMode(); }
            }
            if res {
              unorderedCopy(t, true);
            }
          }
        }
      }
      return truth;
    }

    proc isSorted(): bool {
      var res = true; // strings are sorted?
      // Is this position done comparing with its predecessor?
      var done: [offsets.aD] bool;
      // First string has no predecessor, so comparison is automatically done
      done[offsets.aD.low] = true;
      // Do not check null terminators
      const lengths = getLengths() - 1;
      const maxLen = max reduce lengths;
      ref oa = offsets.a;
      ref va = values.a;
      // Compare each pair of strings byte-by-byte
      for pos in 0..#maxLen {
        forall (o, l, d, i) in zip(oa, lengths, done, offsets.aD) with (ref res) {
          if (!d) {
            // If either of the strings is exhausted, mark this entry done
            if (pos >= l) || (pos >= lengths[i-1]) {
              unorderedCopy(d, true);
            } else {
              const prevByte = va[oa[i-1] + pos];
              const currByte = va[o + pos];
              // If we can already tell the pair is sorted, mark done
              if (prevByte < currByte) {
                unorderedCopy(d, true);
              // If we can tell the pair is not sorted, the return is false
              } else if (prevByte > currByte) {
                res = false;
              } // If we can't tell yet, keep checking
            }
          }
        }
        // If some pair is not sorted, return false
        if !res {
          return false;
        // If all comparisons are conclusive, return true
        } else if (&& reduce done) {
          return true;
        } // else keep going
      }
      // If we get to this point, it's because there is at least one pair of strings with length maxLen that are the same up to the last byte. That last byte determines res.
      return res;
    }

    proc argsort(checkSorted:bool=true): [offsets.aD] int throws {
      const ref D = offsets.aD;
      const ref va = values.a;
      if checkSorted && isSorted() {
        var ranks: [D] int = [i in D] i;
        return ranks;
      }
      var ranks = twoPhaseStringSort(this);
      return ranks;
    }

  } // class SegString

  enum SearchMode { contains, startsWith, endsWith }
  class UnknownSearchMode: Error {}
  
  inline proc segmentContains(const ref values: [?D] uint(8), const ref substr: string): bool {
    var subInd = 1;
    // Slide the substring over the bytes in this segment
    for (byte, i) in zip(values, 0..) {
      if (substr.numBytes - subInd + 1 > values.size - i) {
        return false;
      }
      if (byte != substr.byte[subInd]) {
        // Start over
        subInd = 1;
      } else {
        if (subInd == substr.numBytes) {
          // Eureka
          return true;
        } else {
          // Keep going
          subInd += 1;
        }
      }
    }
    return false;
  }

  inline proc segmentStartsWith(const ref values: [?D] uint(8), const ref substr: string): bool {
    // Caller guarantees that values is at least as long as substr
    for (vbyte, sbyte) in zip(values[{D.low..#substr.numBytes}], substr.chpl_bytes()) {
      if (vbyte != sbyte) {
        return false;
      }
    }
    return true;
  }

  inline proc segmentEndsWith(const ref values: [?D] uint(8), const ref substr: string): bool {
    // Caller guarantees that values is at least as long as substr
    for (vbyte, sbyte) in zip(values[{(D.high-substr.numBytes+1)..#substr.numBytes}], substr.chpl_bytes()) {
      if (vbyte != sbyte) {
        return false;
      }
    }
    return true;
  }
  
  /* Test for equality between two same-length arrays of strings. Returns
     a boolean vector of the same length. */
  proc ==(lss:SegString, rss:SegString) throws {
    // String arrays must be same size
    if (lss.size != rss.size) {
      throw new owned ArgumentError();
    }
    ref oD = lss.offsets.aD;
    var truth: [oD] bool;
    // Early exit for zero-length result
    if (lss.size == 0) {
      return truth;
    }
    ref lvalues = lss.values.a;
    ref loffsets = lss.offsets.a;
    ref rvalues = rss.values.a;
    ref roffsets = rss.offsets.a;
    // Compare segments in parallel
    // Segments are guaranteed to be on same locale, but bytes are not
    forall (t, lo, ro, idx) in zip(truth, loffsets, roffsets, oD) {
      var llen: int;
      var rlen: int;
      if (idx == oD.high) {
        llen = lvalues.size - lo - 1;
        rlen = rvalues.size - ro - 1;
      } else {
        llen = loffsets[idx+1] - lo - 1;
        rlen = roffsets[idx+1] - ro - 1;
      }
      // Only compare bytes if lengths are equal
      if (llen == rlen) {
        var allEqual = true;
        // TO DO: consider an on clause here to ensure at least one access is local
        for pos in 0..#llen {
          if (lvalues[lo+pos] != rvalues[ro+pos]) {
            allEqual = false;
            break;
          }
        }
        // Only if lengths and all bytes are equal, set result to true
        if allEqual {
          unorderedCopy(t, true);
        }
      }
    }
    return truth;
  }

  /* Test an array of strings for equality against a constant string. Return a boolean
     vector the same size as the array. */
  proc ==(ss:SegString, testStr: string) {
    ref oD = ss.offsets.aD;
    // Initialize to true, then set non-matching entries to false along the way
    var truth: [oD] bool = true;
    // Early exit for zero-length result
    if (ss.size == 0) {
      return truth;
    }
    ref values = ss.values.a;
    ref vD = ss.values.aD;
    ref offsets = ss.offsets.a;
    // Use a whole-array strategy, where the ith byte from every segment is checked simultaneously
    // This will do len(testStr) parallel loops, but loops will have low overhead
    for (b, i) in zip(testStr.chpl_bytes(), 0..) {
      [(t, o, idx) in zip(truth, offsets, oD)] if ((o+i > vD.high) || (b != values[o+i])) {unorderedCopy(t, false);}
    }
    // Check the length by checking that the next byte is null
    [(t, o, idx) in zip(truth, offsets, oD)] if ((o+testStr.size > vD.high) || (0 != values[o+testStr.size])) {unorderedCopy(t, false);}
    return truth;
  }

  /* Test array of strings for membership in another array (set) of strings. Returns
     a boolean vector the same size as the first array. */
  proc in1d(mainStr: SegString, testStr: SegString, invert=false, hashKey=defaultSipHashKey) throws where useHash {
    var truth: [mainStr.offsets.aD] bool;
    // Early exit for zero-length result
    if (mainStr.size == 0) {
      return truth;
    }
    // Hash all strings for fast comparison
    const hashes = mainStr.hash(hashKey);
    if v {writeln("Making associative domains for test set on each locale"); stdout.flush();}
    var t1 = getCurrentTime();
    // On each locale, make an associative domain with the hashes of the second array
    // parSafe=false because we are adding in serial and it's faster
    var localTestHashes: [PrivateSpace] domain(2*uint(64), parSafe=false);
    coforall loc in Locales {
      on loc {
        // Local hashes of second array
        ref mySet = localTestHashes[here.id];
        mySet.requestCapacity(testStr.size);
        const testHashes = testStr.hash(hashKey);
        for h in testHashes {
          mySet += h;
        }
        /* // Check membership of hashes in this locale's chunk of the array */
        /* [i in truth.localSubdomain()] truth[i] = mySet.contains(hashes[i]); */
      }
    }
    if v {
      writeln(getCurrentTime() - t1, " seconds");
      writeln("Testing membership"); stdout.flush();
      t1 = getCurrentTime();
    }
    [i in truth.domain] truth[i] = localTestHashes[here.id].contains(hashes[i]);
    if v {writeln(getCurrentTime() - t1, " seconds"); stdout.flush();}
    return truth;
  }

  private config const in1dSortThreshold = 64;
  
  proc in1d(mainStr: SegString, testStr: SegString, invert=false) throws where !useHash {
    var truth: [mainStr.offsets.aD] bool;
    // Early exit for zero-length result
    if (mainStr.size == 0) {
      return truth;
    }
    if (testStr.size <= in1dSortThreshold) {
      for i in 0..#testStr.size {
        truth |= (mainStr == testStr[i]);
      }
      return truth;
    } else {
      /* // This is inspired by numpy in1d */
      /* const (uMain, revIdx) = mainStr.unique(returnInverse=true); */
      /* const uTest = testStr.unique(); */
      /* const ar = concat(uMain, uTest); */
      /* const order = ar.argsort(); */
      /* const sar = ar[order]; */
      /* var flag: [sar.domain] bool; */
      /* const first = sar.domain.low; */
      /* const last = sar.domain.high; */
      /* flag[last] = invert; */
      /* if invert { */
      /*   flag[first..last-1] = (sar[first+1..last] != sar[first..last-1]); */
      /* } else { */
      /*   flag[first..last-1] = (sar[first+1..last] == sar[first..last-1]); */
      /* } */
      /* var ret: [sar.domain] bool; */
      /* [(ord, f) in zip(order, flag)] if f { unorderedCopy(ret[ord], true) }; */
      /* unorderedCopyTaskFence(); */
      /* var realRet: [mainStr.offsets.aD] bool; */
      /* [(r, i) in zip(realRet, revIdx)] unorderedCopy(r, ret[i]); */
      /* unorderedCopyTaskFence(); */
      /* return realRet; */

      if v {writeln("Making associative domains for test set on each locale"); stdout.flush();}
      var t1 = getCurrentTime();
      // On each locale, make an associative domain with the hashes of the second array
      // parSafe=false because we are adding in serial and it's faster
      var localTestDoms: [PrivateSpace] domain(string, parSafe=false);
      coforall loc in Locales {
        on loc {
          const myTestStr = testStr;
          // Local hashes of second array
          ref mySet = localTestDoms[here.id];
          mySet.requestCapacity(testStr.size);
          for i in myTestStr.offsets.aD {
            mySet += myTestStr[i];
          }
        /* // Check membership of hashes in this locale's chunk of the array */
        /* [i in truth.localSubdomain()] truth[i] = mySet.contains(hashes[i]); */
      }
    }
    if v {
      writeln(getCurrentTime() - t1, " seconds");
      writeln("Testing membership"); stdout.flush();
      t1 = getCurrentTime();
    }
    forall i in truth.domain {
      truth[i] = localTestDoms[here.id].contains(mainStr[i]);
    }
    if v {writeln(getCurrentTime() - t1, " seconds"); stdout.flush();}
    return truth;
    }
  }

  /* Convert an array of raw bytes into a Chapel string. */
  inline proc interpretAsString(bytearray: [?D] uint(8)): string {
    // Byte buffer must be local in order to make a C pointer
    var localBytes: [0..#D.size] uint(8) = bytearray;
    var cBytes = c_ptrTo(localBytes);
    // Byte buffer is null-terminated, so length is buffer.size - 1
    // The contents of the buffer should be copied out because cBytes will go out of scope
    // var s = new string(cBytes, D.size-1, D.size, isowned=false, needToCopy=true);
    var s = createStringWithNewBuffer(cBytes, D.size-1, D.size);
    return s;
  }
}