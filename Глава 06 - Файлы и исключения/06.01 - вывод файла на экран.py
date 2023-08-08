infile = open(r'data\numbers.txt', 'r')

for line in infile:
    print(f'{line.rstrip()}')

infile.close()