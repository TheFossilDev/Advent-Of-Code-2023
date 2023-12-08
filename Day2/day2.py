'''
SAMPLE INPUT:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
NUM_RED, NUM_GREEN, NUM_BLUE = 12, 13, 14
def isInvalid(r, g, b):
  return r > NUM_RED or g > NUM_GREEN or b > NUM_BLUE

# inputFile = open("Day2/sample-input.txt", "r")
inputFile = open("Day2/sample-input.txt", "r")

def partOne(inputFile):
  validSum = 0
  for line in inputFile:
    gameID, gameValues = line.split(":")
    gameID = gameID.split()[1] # A little nasty
    gamePulls = gameValues.split(";")
    pullInvalid = False
    for pull in gamePulls:
      diceCounts = {"red": 0, "green": 0, "blue": 0}
      dice = pull.split(",")
      for die in dice:
        # Add the dice
        count, color = die.split()
        diceCounts[color] += eval(count)
      # Validate
      if isInvalid(diceCounts["red"], diceCounts["green"], diceCounts["blue"]):
        pullInvalid = True
        break
    if not pullInvalid:
      validSum += eval(gameID)
  print("Sum:", validSum)


def partTwo(inputFile):
  powerSum = 0
  for game in inputFile:
    gameID, gameValues = game.split(":")
    gameID = gameID.split()[1] # A little nasty
    gamePulls = gameValues.split(";")
    diceMins = {"red": 0, "green": 0, "blue": 0}
    for pull in gamePulls:
      dice = pull.split(",")
      for die in dice:
        count, color = die.split()
        # If you had 2 red and found 4 red, then you need 4 as your minimum
        diceMins[color] = max(eval(count), diceMins[color])
    gamePower = diceMins["red"] * diceMins["green"] * diceMins["blue"]
    print(f"Game {gameID} power: {gamePower}")
    powerSum += gamePower
  print(powerSum)


# partOne(inputFile)
partTwo(inputFile)