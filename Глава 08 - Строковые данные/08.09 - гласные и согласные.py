VOWELS = "АЕЁИОУЫЭЮЯ"
CONSONANTS = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

def count_vowels(string:str)-> int:
    number = 0
    for char in string:
        if char.upper() in VOWELS:
            number +=1
    return number


def count_consonants(string:str)->int:
    number = 0
    for char in string:
        if char.upper() in CONSONANTS:
            number += 1
    return number


def main():
    input_string = input("Введите строку: ")
    vowels_quantity = count_vowels(input_string)
    consonants_quantity = count_consonants(input_string)
    print(f"В этой строке {vowels_quantity} гласных и {consonants_quantity} согласных букв")


if __name__ == '__main__':
    main()