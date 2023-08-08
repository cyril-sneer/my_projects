def rec_pow(num, pw):
    if pw == 0:
        return 1
    else:
        return num * rec_pow(num, pw - 1)

def main():
    num = float(input("Введите число: "))
    pw = int(input("Введите степень: "))
    print(rec_pow(num, pw))

if __name__ == '__main__':
    main()