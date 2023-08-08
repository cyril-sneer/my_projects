infile = open(r'data\names.txt', 'r')

counter = 0
for line in infile:
    counter += 1

print(counter)

infile.close()