input_string = input("Введите строку: ")

out_string = input_string[0]
for char in input_string[1:]:
    if char.isupper():
        out_string += " " + char.lower()
    else:
        out_string += char

print(out_string)
