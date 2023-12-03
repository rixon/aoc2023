#!/opt/homebrew/bin/python3

filename="test.input"
gamelist = []


def loadfile(filename):
  myfile = open(filename, 'r')

  for line in myfile:
    games.append(line)
  
  return games

def parse_game(thisgame):
  gamenum=thisgame.split(":")[0].split()[1]
  plays=thisgame.split(":")[1].split(";")
  play1=plays[0]
  play2=plays[1]
  play3=plays[2]
  for play in range(0,3):
    # We'll have red, blue, and/or green, but not necessarily all three.
    colors=play.split(',')
    for color in colors:
      if color.split()[0]
