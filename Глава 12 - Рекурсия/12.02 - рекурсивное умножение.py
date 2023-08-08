def rec_mult(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + rec_mult(x, y - 1)

def main():
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    print(rec_mult(x, y))

main()