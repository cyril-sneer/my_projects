def kinetic_energy(m, v):
    return (m * v ** 2) / 2

def main():
    mass = float(input('Введите массу тела в кг:\t\t'))
    velocity = float(input('Введите скорость тела в м/с:\t'))

    energy = kinetic_energy(mass, velocity)

    print(f'Кинетическая энергия тела равна {energy:.2f} Дж')


main()
