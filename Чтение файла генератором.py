with open(r'Глава 09 - Словари и множества/data/Kennedy.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)


f = open(r'Глава 09 - Словари и множества/data/Kennedy.txt', 'r')
lines = (line.strip() for line in f)
for line in lines:
    print(line)
f.close()
