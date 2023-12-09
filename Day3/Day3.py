'''
Sample input
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

- Still wanting to do a left-right read because it helps identify numbers
- Need some kind of math relation to find this...

..*..
.123.
.....
^   ^
i   j
i = StartOfWord - 1
j = StartOfWord + len(word)

'''
# inputFile = open("Day3/sample-input.txt", "r")
inputFile = open("Day3/input.txt", "r")
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
board = inputFile.read().strip().split("\n")
BOARD_LENGTH, BOARD_HEIGHT = len(board[0]), len(board)

def twoDPrinter(board):
  for line in board:
    for col in line:
      print(col, end="")
    print()

def inBounds(i, length):
  return i >= 0 and i < length

def isPart(i):
  return i not in NUMBERS and i != "."

def findEnginePart(boardY, l, r, boardLength, boardHeight):
  '''
  ..*..
  .123.
  .....
   ^ ^
   i j
  i = StartOfWord
  j = StartOfWord + len(word) - 1
  '''
  # print(f"xl={l} xr={r} y={boardY} len={boardLength} hei={boardHeight}")
  # Scan top
  # Check top OOB
  if inBounds(boardY-1, boardHeight):
    for i in range(l-1, r+2):
      if inBounds(i, boardLength) and isPart(board[boardY-1][i]):
        return True
  # Scan sides
  if inBounds(l-1, boardLength) and isPart(board[boardY][l-1]):
    return True
  if inBounds(r+1, boardLength) and isPart(board[boardY][r+1]):
    return True
  # Scan bottom
  # Check bottom OOB
  if inBounds(boardY+1, boardHeight):
    for i in range(l-1, r+2):
      print("line=",boardY, i, boardLength)
      if inBounds(i, boardLength) and isPart(board[boardY+1][i]):
        return True
  return False

def partOne(board):
  partSum = 0
  for boardY, line in enumerate(board):
    # Find a number, find the left and right of the number, scan
    i = 0
    while i<len(line):
      if line[i] not in NUMBERS:
        i+=1
      else:
        j = i+1
        while j<len(line) and line[j] in NUMBERS:
          j+=1
        if findEnginePart(boardY, i, j-1, len(line), len(board)): # Give l, r of WORD
          print(line[i:j] + " is a part")
          partSum += eval(line[i:j]) # OBO Caution
        i = j
  print(partSum)

def wordSearch(charX, charY, searchedCells):
  # Returns number found
  word = board[charY][charX]
  searchedCells[charY][charX] = 1
  l, r = charX-1, charX+1
  # print(f"Word: l={board[charY][l]} r={board[charY][r]}")
  # Scan left
  while inBounds(l, BOARD_LENGTH) and not searchedCells[charY][l] and board[charY][l] in NUMBERS:
    word = board[charY][l] + word
    # print("Added l",word)
    searchedCells[charY][l] = 1
    l-=1
  # Scan right
  while inBounds(r, BOARD_LENGTH) and not searchedCells[charY][r] and board[charY][r] in NUMBERS:
    word = word + board[charY][r]
    # print("Added r",word)
    searchedCells[charY][r] = 1
    r+=1
  # print("Final", word)
  return eval(word)

def gearRatioSearch(gearX, gearY):
  # Returns -1 if NOT 2 GEARS is found
  # Maintain which cells have been searched
  numbersFound = 0
  numbers = []
  gearRatio = 1
  searchedCells = [[0 for _ in range(BOARD_LENGTH)] for _ in range(BOARD_HEIGHT)]

  # GROSS but not feeling like a refactor right now
  # Check top
  # TOP LEFT
  if inBounds(gearX-1, BOARD_LENGTH) and inBounds(gearY-1, BOARD_HEIGHT) and not searchedCells[gearY-1][gearX-1] and board[gearY-1][gearX-1] in NUMBERS:
    res = wordSearch(gearX-1, gearY-1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # TOP MIDDLE
  if inBounds(gearX, BOARD_LENGTH) and inBounds(gearY-1, BOARD_HEIGHT) and not searchedCells[gearY-1][gearX] and board[gearY-1][gearX] in NUMBERS:
    res = wordSearch(gearX, gearY-1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # TOP RIGHT
  if inBounds(gearX+1, BOARD_LENGTH) and inBounds(gearY-1, BOARD_HEIGHT) and not searchedCells[gearY-1][gearX+1] and board[gearY-1][gearX+1] in NUMBERS:
    res = wordSearch(gearX+1, gearY-1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # Check sides
  # LEFT
  if inBounds(gearX-1, BOARD_LENGTH) and inBounds(gearY, BOARD_HEIGHT) and not searchedCells[gearY][gearX-1] and board[gearY][gearX-1] in NUMBERS:
    res = wordSearch(gearX-1, gearY, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # RIGHT
  if inBounds(gearX+1, BOARD_LENGTH) and inBounds(gearY, BOARD_HEIGHT) and not searchedCells[gearY][gearX+1] and board[gearY][gearX+1] in NUMBERS:
    res = wordSearch(gearX+1, gearY, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # Check bottom
  # BOTTOM LEFT
  if inBounds(gearX-1, BOARD_LENGTH) and inBounds(gearY+1, BOARD_HEIGHT) and not searchedCells[gearY+1][gearX-1] and board[gearY+1][gearX-1] in NUMBERS:
    res = wordSearch(gearX-1, gearY+1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # BOTTOM MIDDLE
  if inBounds(gearX, BOARD_LENGTH) and inBounds(gearY+1, BOARD_HEIGHT) and not searchedCells[gearY+1][gearX] and board[gearY+1][gearX] in NUMBERS:
    res = wordSearch(gearX, gearY+1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # BOTTOM RIGHT
  if inBounds(gearX+1, BOARD_LENGTH) and inBounds(gearY+1, BOARD_HEIGHT) and not searchedCells[gearY+1][gearX+1] and board[gearY+1][gearX+1] in NUMBERS:
    res = wordSearch(gearX+1, gearY+1, searchedCells)
    gearRatio *= res
    numbers.append(res)
    numbersFound += 1
  # Reset board after search
  if numbersFound == 2:
    # print(f"FOUND at {gearX+1},{gearY+1} Numbers {numbers}")
    print(numbers)
    return gearRatio
  else:
    print(f"INVALID at {gearX+1},{gearY+1} because found {numbersFound}. Numbers {numbers}")
    return -1

def partTwo(board):
  gearRatioSum = 0
  for y, line in enumerate(board):
    # Find a gear and then do a surrounding search
    for x, char in enumerate(line):
      if char == "*":
        gearRatio = gearRatioSearch(x,y)
        if gearRatio != -1:
          gearRatioSum += gearRatio
          print(gearRatioSum)
  print(gearRatioSum)

# twoDPrinter(board)

# partOne(board)
partTwo(board)
# twoDPrinter(searchedCells)
