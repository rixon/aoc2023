#!/opt/homebrew/bin/python3

filename="3a.input"
gamelist = []

def loadfile(filename):
  myfile = open(filename, 'r')
  lines=[]

  for line in myfile:
    lines.append(line.strip())
  
  return lines
  myfile.close()

def parse_line(thisline):
  in_number = False
  # pnums (Part Numbers) will be a list of tuples (part_num, start_posn)
  pnums=[]
  # parts will be a list of tuples (part_char, posn)
  parts=[]
  new_num=""

  for i, c in enumerate(thisline):
    if c.isdigit():
      if not in_number:
        in_number = True
        start_pos = i
      new_num+=c
    elif c == ".":
      # null value; noop.
      if in_number:
        # End the part number; save it.
        in_number=False
        pnums.append((new_num, start_pos))
        new_num=""
    else:
      # implied symbol - this is a part.
      parts.append((c, i))
      if in_number:
        # End the part number; save it.
        in_number=False
        pnums.append((new_num, start_pos))
        new_num=""
  
  # Save the last number (if it's the end of line)
  if in_number:
    pnums.append((new_num, start_pos))
  return(pnums, parts)

def find_ratio(gearloc, linenum):
  is_part=False
  # Scan for nearby partnums.
  start_position = gearloc
  pnums=[]
  ratio=0
  # Look for partnum in spos-1 to spos+1 on line-1, line, and line+1
  # If found, is_part=True
  print("Checking for gear candidate for ", gearloc, "in lines ", linenum-1, "through", linenum+2)
  for i in range(linenum-1, linenum+2):
    print("  Checking line", i)
    if 0 <= i < len(partlist):
      for j in partlist[i]:
        #print("  Checking if", start_position-1, "<=", j[1], "<=", (j[1] + len(j[0])), "<=", start_position+1)
        #if (start_position - 1) <= j[1] <= (j[1] + len(j[0])) <= (start_position + 1):
        print("  Checking if", j[0], "at", j[1], "contains", gearloc)
        if gearloc in range((j[1] - 1), (j[1] + len(j[0]) + 1)):
          print("   ", j[0], "is a part num!")  
          pnums.append(int(j[0]))
        else:
          print("   is NOT a part num.")  
  

  if len(pnums) == 2:
    #is_part=True
    print("Saving gear ratio components", pnums)
    ratio=(pnums[0] * pnums[1])

  return ratio


lines_to_parse = loadfile(filename)

partlist=[]
schematic=[]
for line in lines_to_parse:
  print(line)
  parsed_line=parse_line(line)
  # partlist: Each of the part number candidate tuples. List of lines; each line is list of tuples of (pnum, start_pos)
  partlist.append(parsed_line[0])
  # schematic: Each of the part locations. List of lines; each line list of positions.
  schematic.append(parsed_line[1])

print()
print("Part list: ", partlist)
print("Schematic: ", schematic)
print()

tally=0
for linenum in range(0,len(schematic)):
  line = schematic[linenum]
  #print("Working with line: ", line)
  for part in line:
    if part[0] == '*':
      gear_ratio = find_ratio(part[1], linenum)

      if gear_ratio > 0:
        print(part, " is a gear with a ratio!")
      else:
        print(part, " is NOT a part.")
      tally += gear_ratio

print("Final tally is ", tally)


