#!/opt/homebrew/bin/python3

filename="1a.input"
gamelist = []
numbers = {'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9}

def loadfile(filename):
  myfile = open(filename, 'r')
  lines=[]

  for line in myfile:
    lines.append(line.strip())

  return lines
  myfile.close()

def parseline(line):
  linedigits=[]
  linelen=len(line)
  for i in range(0, linelen):
    char=line[i]
    key = None
    word1 = None
    word2 = None
    word3 = None
    if char.isdigit():
      linedigits.append(int(char))
      print("FOUND", char)
      continue
    else:
      # It's a letter... let's do a keyword scan.
      print(" Trying letter", char, "at posn", i,"line len", linelen)
      if i < (linelen - 2):
        word1=char+line[i+1]+line[i+2]
      if i < (linelen - 3):
        word2=word1+line[i+3]
      if i < (linelen - 4):
        word3=word2+line[i+4]
      print("  WORD1:", word1,"  WORD2:", word2,"  WORD3:", word3)
      for key in (word1, word2, word3):
        if key in numbers:
          linedigits.append(numbers[key])
          print("  FOUND:",linedigits[-1])  
          break
      #if any(m=n for m in (word1, word2, word3) for n in numbers):
      #  linedigits.append(numbers[(word1, word])
      #  print("FOUND", word1, "APPENDED", linedigits[-1])
      #  continue
      #elif any(word2 in j for j in numbers):
      #  linedigits.append(numbers[word2])
      #  print("FOUND", word2, "APPENDED", linedigits[-1])
      # 	continue
      #elif any(word3 in j for j in numbers):
      #  linedigits.append(numbers[word3])
      #  print("FOUND", word3, "APPENDED", linedigits[-1])

  return linedigits


mymap=loadfile(filename)
tally=0
print(mymap)
for line in mymap:
  print("Working with line", line)
  digits = parseline(line)
  print("  Got digits", digits)
  line_num = int(str(digits[0])+str(digits[-1]))
  tally += line_num
  print("    Resulting operand:", line_num, " Tally:", tally)

print(tally)
