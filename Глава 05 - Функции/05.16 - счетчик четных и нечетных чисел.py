import random


def calc_evens_odds(num_list: list) -> tuple[int, int]:
    ev = od = 0
    for n in num_list:
        if n % 2 == 0: ev += 1
        else: od += 1
    return ev, od


def main():
    numbers = [ random.randint(1, 100) for i in range(20) ]
    print(numbers)
    evens, odds = calc_evens_odds(numbers)
    print(f'Четных: {evens:d}, Нечетных: {odds:d}')


main()
