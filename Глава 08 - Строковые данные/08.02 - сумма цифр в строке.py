def main():
    number_as_string = input("Введите число: ")

    # _sum = 0
    # for ch in number_as_string:
    #     _sum += int(ch)

    numbers_list = [int(ch) for ch in number_as_string]
    _sum = sum(numbers_list)

    print(f"Сумма цифр числа равна: {_sum}")

if __name__ == '__main__':
    main()