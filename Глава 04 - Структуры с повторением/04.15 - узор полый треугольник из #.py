character = '#'
size = 6

for i in range(size):
    print(character, end='')
    for j in range(i):
        print(' ', end='')
    print(character)
