import os

print("File Parser")
opf = open('parsedop.txt', 'w')
file = raw_input("Please enter file name::")
text = raw_input("Please enter text to parse::")
with open(file) as f:
    for line in f:
         if text in line:
		opf.write(line)
		opf.write('\n')
opf.close()
f.close()

