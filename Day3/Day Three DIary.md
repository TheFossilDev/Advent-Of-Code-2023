# Day 3

## Part One

Chased down a rabbit hole of a bug and it turned out to be a simple error resulting from the input file ending with a new line. I literally just added `strip()` and it was fine lol

## Part Two

**WOW** the folks were right about odd numbered days having a twist. I had a sneaking suspicion this was a graph problem and then lo and behold a graph problem in the second half. Completely regretting my very barebones solution to part one now. Oh well I love practicing graph stuff

---

_Wait a second_... I think I can still do this in a non-graph way. First find a gear...

```
467..114..
...*......
..35......
```

Then search its surroundings. Count the numbers it hits. If it's two, scan left to right to grab the number.

- Works for N, NE, NW, W, E, S, SW, SE. _Wow! can't wait til morning to finish_

## After completion

_Wow_ lots of lessons learned. Made some simple mistakes and gave my first incorrect submission after thinking it correct. The finished code is quite a beast that could be simplified and made better. 2D Array walks are not my forte so something to practice for sure
