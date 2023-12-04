#!/opt/homebrew/bin/python3

filename="1a.input"
gamelist = []

def loadfile(filename):
  myfile = open(filename, 'r')
  lines=[]

  for line in myfile:
    lines.append(line.strip())

  return lines
  myfile.close()

def parseline(line):
  linedigits=[]
  for char in line:
    if char.isdigit():
      linedigits.append(char)

  return linedigits


mymap=loadfile(filename)
tally=0
print(mymap)
for line in mymap:
  print("Working with line", line)
  digits = parseline(line)
  print("  Got digits", digits)
  line_num = int(digits[0]+digits[-1])
  tally += line_num
  print("    Resulting operand:", line_num, " Tally:", tally)

print(tally)
