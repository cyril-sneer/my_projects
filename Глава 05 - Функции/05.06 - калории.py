def main():
    fats = float(input('Введите количество жиров:\t\t'))
    carbohydrates = float(input('Введите количество углеводов:\t'))

    calories = calc_calories(fats, carbohydrates)

    print(f'\nВы потребили {calories:.1f} калорий')


def calc_calories(f:float, c:float) -> float:
    return f * 9 + c * 4


main()