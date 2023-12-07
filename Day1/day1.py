'''
Input: multiple lines of text where each line contains a left and (or) right digit 
and a random amount of characters both digits and a-z


Output: Sum of all extracted digits from input
Example input:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

Example output: 12 + 38 + 15 + 77 = 142

Approaches:
1. Left to right slide. Find first number then slide replacing the right number with furthest along
2. Regex pattern match
3. Regex strip chars off side then take [0] and [-1]

PART TWO Example Input
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

'''
# inputFile = open("Day1/input.txt", "r")
inputFile = open("Day1/input.txt", "r")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
wordNumbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}
total = 0

# def extractDigit(line):
#   leftDigit = ""
#   rightDigit = ""
#   foundLeftDigit = False
#   for char in line:
#     # What's the best approach for type checking?
#     # I want to avoid a hard type check
#     if char in numbers:
#       if not foundLeftDigit:
#         foundLeftDigit = True
#         leftDigit = char
#         rightDigit = char
#       else:
#         rightDigit = char
#   lineSum = eval(leftDigit + rightDigit)
#   print(lineSum)
#   return lineSum
def isLessThanLen(sA, sB, a, b):
  return a < len(sA) and b < len(sB)

def extractDigitTwo(line):
  leftDigit = ""
  rightDigit = ""
  foundLeftDigit = False
  for i, char in enumerate(line):
    if char in numbers:
      if not foundLeftDigit:
        leftDigit = char
        foundLeftDigit = True
      rightDigit = char
    else:
      # Try each word
      for word in wordNumbers.keys():
        j = i
        wordI = 0
        matchString = ""
        while isLessThanLen(word, line, wordI, j) and word[wordI] == line[j]:
          # They are matching
          matchString += line[j]
          if wordI == len(word)-1:
            # They matched
            print("Found", matchString)
            rightDigit = wordNumbers[matchString]
            if not foundLeftDigit:
              leftDigit = wordNumbers[matchString]
              foundLeftDigit = True
          wordI += 1
          j += 1
  # End line
  lineSum = eval(leftDigit + rightDigit)
  print(lineSum)
  return lineSum


for line in inputFile:
  # lineSum = extractDigit(line)
  lineSum = extractDigitTwo(line)
  total += lineSum
print("Total =", total)


