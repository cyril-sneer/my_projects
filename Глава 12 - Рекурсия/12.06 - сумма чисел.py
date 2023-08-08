def rec_sum(num: int):
    if num == 0:
        return 0
    else:
        return num + rec_sum(num - 1)

def main():
    num = int(input("Введите целое число: "))
    print(rec_sum(num))

main()