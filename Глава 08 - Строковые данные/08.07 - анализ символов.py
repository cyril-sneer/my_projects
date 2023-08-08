INPUT_FILE_NAME = r"data\text.txt"

input_file = open(INPUT_FILE_NAME, 'r')
# sentences = [string.rstrip() for string in input_file.readlines()]
sentences = input_file.readlines()
input_file.close()

upper_symbols = 0
lower_symbols = 0
digit_symbols = 0
space_symbols = 0

for item in sentences:
    for char in item:
        if char.isupper(): upper_symbols += 1
        if char.islower(): lower_symbols += 1
        if char.isdigit(): digit_symbols += 1
        if char.isspace(): space_symbols += 1

print(f'Upper symbols = {upper_symbols}')
print(f'Lower symbols = {lower_symbols}')
print(f'Digit symbols = {digit_symbols}')
print(f'Space symbols = {space_symbols}')
