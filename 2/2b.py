#!/opt/homebrew/bin/python3

filename="2a.input"
gamelist = []
gamestats=[]


def loadfile(filename):
  myfile = open(filename, 'r')

  games=[]
  for line in myfile:
    games.append(line.strip())
  
  return games

def parse_game(thisgame):
  print("Working with game", thisgame)
  gamenum=int(thisgame.split(":")[0].split()[1])
  print(" Game number:", gamenum)
  gameplays=[]
  plays=thisgame.split(":")[1].split(";")
  #play1=plays[0] play2=plays[1] play3=plays[2]
  print(" Plays for this game:", plays)
  for play in plays:
    color_count=[0, 0, 0]
    print("  Play:", play)
    # We'll have red, blue, and/or green, but not necessarily all three.
    colors=play.split(',')
    for color in colors:
      thiscolor = color.split()
      print("   Color:", thiscolor)
      if thiscolor[1].strip() == "red":
        color_count[0] = int(thiscolor[0])
      elif thiscolor[1].strip() == "green":
        color_count[1] = int(thiscolor[0])
      elif thiscolor[1].strip() == "blue":
        color_count[2] = int(thiscolor[0])
      else:
        print("YOU SHOULD NOT SEE THIS")
    gameplays.append(color_count)
  return (gamenum, gameplays)

def find_max_per_color(game):
  plays = game[1]
  red = 0
  green = 0
  blue = 0
  for play in plays:
    if play[0] > red:
      red = play[0]
    if play[1] > green:
      green = play[1]
    if play[2] > blue:
      blue = play[2]
  return (red, green, blue)

gamelist=loadfile(filename)

for game in gamelist:
  gamestats.append(parse_game(game))

tally=0
for game in gamestats:
  max_red = 12
  max_green = 13
  max_blue = 14
  max_colors = find_max_per_color(game)
  #if (max_colors[0] <= max_red) and (max_colors[1] <= max_green) and (max_colors[2] <= max_blue):
  #  game_possible = True
  #  print ("Game", game[0], ": Is possible.")
  #  tally += game[0]
  #else:
  #  print ("Game", game[0], ": Is NOT possible.")
  power = (max_colors[0] * max_colors[1] * max_colors[2])
  print ("Game", game[0], power)
  tally += power

print("Tally of games:", tally)

