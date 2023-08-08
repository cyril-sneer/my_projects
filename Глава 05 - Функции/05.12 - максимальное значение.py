def max_(num1, num2):
    return num1 if num1 > num2 else num2

def main():
    num1 = int(input('Введите первое число:\t'))
    num2 = int(input('Введите второе число:\t'))

    print(f'\n{max_(num1, num2)} является бОльшим из введенных чисел')

main()