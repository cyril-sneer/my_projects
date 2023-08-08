def km2miles(km):
    return km * 0.6214

def main():
    km = float(input('Введите расстояние в километрах:\t'))
    print(f'Расстояне в милях:\t{km2miles(km):.4f}')

if __name__ == '__main__':
    main()
