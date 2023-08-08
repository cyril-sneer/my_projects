class Pet:
    def __init__(self, name:str, animal_type:str, age:int):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    my_pet = Pet(None, None, None)
    name = input("Введите имя животного: ")
    animal_type = input("Введите тип животного: ")
    age = int(input("Введите возраст животного: "))
    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print()
    print(f'Имя животного - {my_pet.get_name()}')
    print(f'Тип животного - {my_pet.get_animal_type()}')
    print(f'Возраст животного - {my_pet.get_age()}')

if __name__ == '__main__':
    main()