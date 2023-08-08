# ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# alpha_dict: dict[str, int] = dict(zip(ALPHABET, [0] * len(ALPHABET)))
alpha_dict: dict[str, int] = {}

input_string: str = input('Введите строку: ').replace(' ', '')

for char in input_string:
    alpha_dict.setdefault(char, 0)
    alpha_dict[char] += 1

most_frequent_quantity: int = max(alpha_dict.values())
most_frequent_list = []
for key, value in alpha_dict.items():
    if value == most_frequent_quantity:
        most_frequent_list.append(key)

print(f'Наибольшее частота вхождение - {most_frequent_quantity}, символ/ы: {most_frequent_list}')

print("\n", alpha_dict)
