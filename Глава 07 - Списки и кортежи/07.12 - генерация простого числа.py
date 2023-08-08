import my_funcs

while True:
    test_number = int(input('Введите целое положительное число, 0 - выход: '))
    if test_number == 0: break

    numbers = [i for i in range(2, test_number+1)]

    for n in numbers:
        if my_funcs.is_prime(n): print(f'{n} - простое число')
        else: print(f'{n} - имеет другие делители')