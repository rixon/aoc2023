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
  # parts are just a single char so will just be a list of positions.
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
      parts.append(i)
      if in_number:
        # End the part number; save it.
        in_number=False
        pnums.append((new_num, start_pos))
        new_num=""
  
  # Save the last number (if it's the end of line)
  if in_number:
    pnums.append((new_num, start_pos))
  return(pnums, parts)

def find_nearby_parts(pnum, linenum):
  is_part=False
  # Scan for nearby parts.
  #print("Scanning line", linenum, "for nearby parts.")
  start_position = pnum[1]
  size = len(str(pnum[0]))
  # Look for part in spos-1 to spos+size on line-1, line, and line+1
  # If found, is_part=True
  #print("Checking lines ", linenum-1, "through", linenum+2)
  for i in range(linenum-1, linenum+2):
    #print("Checking line", i)
    if 0 <= i < len(schematic):
      for j in schematic[i]:
        #print("Checking if", start_position, "<=", j, "<=", start_position+size)
        if (start_position - 1) <= j <= (start_position + size):
          #print("is_part!!!")  
          is_part = True
          break
    if is_part:
      break

  return is_part


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
for linenum in range(0,len(partlist)):
  line = partlist[linenum]
  #print("Working with line: ", line)
  for part in line:
    if find_nearby_parts(part, linenum):
      print(part[0], " is a part!")
      tally += int(part[0])
    else:
      print(part[0], " is NOT a part.")

print("Final tally is ", tally)


