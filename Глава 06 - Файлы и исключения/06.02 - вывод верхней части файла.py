infile = open(r'data\numbers.txt', 'r')

line = infile.readline().rstrip()
line_number = 1

while line != '' and line_number <= 5:
    print(line)
    line = infile.readline().rstrip()
    line_number += 1

infile.close()