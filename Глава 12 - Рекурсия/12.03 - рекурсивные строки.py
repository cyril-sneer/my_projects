def rec_print(n):
    if n > 1:
        rec_print(n - 1)
    print("*" * n)

def main():
    n = int(input("Введите целое число: "))
    rec_print(n)

if __name__ == '__main__':
    main()