END_OF_SENTENCE = ".!?"

# input_string = input("Введите предложение: ")
# input_string = input_string[0].upper() + input_string[1:]
# words = input_string.split()
#
# for i in range(len(words)-1):
#     if words[i][-1] in END_OF_SENTENCE:
#         words[i + 1] = words[i + 1][0].upper() + words[i + 1][1:]
#
# output_string = " ".join(words)

# print(f"Ваше приедложение: {output_string}")

def capitalize(string:str)->str:
    new_sentence = True
    out_string = ""

    words = string.split()
    for item in words:
        if new_sentence:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item

        out_string += result_word + " "

        if item[-1] in END_OF_SENTENCE:
            new_sentence = True
        else:
            new_sentence = False

    return out_string


def main():
    input_string = input("Введите предложение: ")
    output_string = capitalize(input_string)
    print(f"Ваше приедложение: {output_string}")


if __name__ == '__main__':
    main()