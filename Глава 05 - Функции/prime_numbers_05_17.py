def is_prime(number: int) -> bool:
    prime = True
    for n in range(2, abs(number)):
        if number % n == 0:
            prime = False
            break
    return prime


def main():
    while True:
        number = int(input('Введите целое число (0 - выход):\t'))
        if number == 0: break
        if is_prime(number): print('Это простое число')
        else: print('Это число не явлется простым')



if __name__ == '__main__':
    main()