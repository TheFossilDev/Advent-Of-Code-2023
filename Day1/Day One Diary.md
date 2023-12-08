# Day 1

## Part One

Input: multiple lines of text where each line contains a left and (or) right digit
and a random amount of characters both digits and a-z

Output: Sum of all extracted digits from input
Example input:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

Example output: 12 + 38 + 15 + 77 = 142

Approaches:

1. Left to right slide. Find first number then slide replacing the right number with furthest along
2. Regex pattern match
3. Regex strip chars off side then take [0] and [-1]

_Simple to begin with. Just started with the first approach for now but this would be a good spot to brush up on #regex eventually_

## Part Two

Change: Now numbers can be considered digits spelled out like _one, two, etc_
_I'm just now realizing I can't just scan letter by letter. Hmmmmm_

> [!WARNING] Careful
> Word digits can overlap: eg _oneight_

Because of needing to progressively try for words and then retry if it doesn't work, this sounds like it could use a [[Trie]]?
_A solution for another time, maybe in Rust. I just want to get this done_

Now the sample input has the word digits

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

### After completion

I did my usual cope of rushing into implementation with only a somewhat idea of my pseudocode in my head. After getting confused by a persistent Pylance error I restarted and did it properly. Just did a fairly inefficient scan of each word within the possible number words on each character and then moved onto the next word. Runtime was still incredibly fast on the real input but good lessons learned for a first day. Glad to be back!
