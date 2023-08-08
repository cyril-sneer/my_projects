ENDING = "КИ"

input_string = input('Введите предложение: ')
words = input_string.split()
out_string = ""

for i in range(len(words)):
    item = words[i].upper()

    if len(item) == 1:
        item += ENDING
    else:
        item = item[1:] + item[0] + ENDING

    out_string = out_string + item + " "

print(out_string)