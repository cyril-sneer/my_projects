character = '*'
size = 7

for i in range(size):
    for j in range(size, i, -1):
        print(character, end='')
    print()

print()

for i in range(size, 0, -1):
    print(character * i)
