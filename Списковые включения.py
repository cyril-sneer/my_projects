spam = [str(number) for number in range(100) if number % 5 != 0]
print(spam)

spam = {str(number) for number in range(100) if number % 5 != 0}
print(spam)

spam = {str(number): number for number in range(100) if number % 5 != 0}
print(spam)

nestedIntList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
nestedStrList = [[str(i) for i in sublist] for sublist in nestedIntList]
print(nestedStrList)


nestedIntList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
nestedStrList = []
for sublist in nestedIntList:
    nestedStrList.append([str(i) for i in sublist])
print(nestedStrList)


nestedList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
flatList = [num for sublist in nestedList for num in sublist]
print(flatList)


nestedList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
flatList = []
for sublist in nestedList:
    for num in sublist:
        flatList.append(num)
print(flatList)

[str(n) for n in [8, 16, 18, 19, 12, 1, 6, 7]]

[n for n in [8, 16, 18, 19, 12, 1, 6, 7] if n % 2 == 0]
