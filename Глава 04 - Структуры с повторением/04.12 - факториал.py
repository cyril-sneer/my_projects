def factorial(number):
    f = 1
    for n in range(1, number+1):
        f *= n
    return f

while True:

    num = -1
    while num < 0:
        num = int(input('Введите число: '))
    if num == 0: break

    print(f'{num}! = {factorial(num):.0f}')