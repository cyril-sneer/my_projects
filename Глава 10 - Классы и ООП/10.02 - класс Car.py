class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def breakk(self):
        if self.__speed > 0:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

def main():
    my_car = Car(2009, "Volkswagen")
    for i in range(5):
        my_car.accelerate()
        print(f"Текущая скорость: {my_car.get_speed()}")

    for i in range(5):
        my_car.breakk()
        print(f"Текущая скорость: {my_car.get_speed()}")

if __name__ == '__main__':
    main()

