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

    words_frequently = {}
    for word in list_of_words:
        # if word in words_frequently:
        #     words_frequently[word] += 1
        # else:
        #     words_frequently[word] = 1
        words_frequently.setdefault(word, 0)
        words_frequently[word] += 1


    for word in words_frequently:
        print(f"{word} : {words_frequently[word]}")

if __name__ == '__main__':
    main()