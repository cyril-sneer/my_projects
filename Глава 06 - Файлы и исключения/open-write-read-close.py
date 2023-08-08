test_file = open(r'data\numbers.txt', 'w')
for i in range(1,11):
    test_file.write(f'{str(i)}\n')
test_file.close()

test_file = open(r'data\numbers.txt', 'r')
line = test_file.readline().rstrip()
while line != '':
    print(line)
    line = test_file.readline().rstrip()
test_file.close()

test_file = open(r'data\numbers.txt', 'r')
for line in test_file:
    print(line.rstrip())


