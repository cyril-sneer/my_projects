import my_funcs

FILE_NAME = r"data\text.txt"

def main():
    in_file = open(FILE_NAME, "r")
    text = in_file.read()
    in_file.close()

    list_of_words = text.split()
    for c in range(len(list_of_words)):
        list_of_words[c] = list_of_words[c].lower()
        list_of_words[c] = list_of_words[c].replace(".", "")
        list_of_words[c] = list_of_words[c].replace(",", "")

    set_of_words = set(list_of_words)
    my_funcs.print_sequence(set_of_words)


if __name__ == '__main__':
    main()