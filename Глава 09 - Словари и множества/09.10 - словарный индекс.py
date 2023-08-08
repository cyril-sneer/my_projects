input_file_name = r"data\Kennedy.txt"
index_file_name = r"data\index_.txt"

def sort_dict_iter(inbound_dict:dict) -> dict:
    sorted_keys = sorted(inbound_dict.keys())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = inbound_dict[key]
    return sorted_dict

def main():
    input_file = open(input_file_name, "r")
    strings = [string.rstrip() for string in input_file.readlines()]
    input_file.close()

    word_index = {}
    str_no = 1
    for string in strings:
        word_list = string.split()
        for word in word_list:
            word_index.setdefault(word, set())
            word_index[word].add(str_no)
        str_no += 1

    word_index = {key.lower():sorted(list(value)) for key, value in word_index.items()}
    word_index = sort_dict_iter(word_index)

    index_file = open(index_file_name, "w")
    for word in word_index:
        out_str = word + ":"
        for i in range(len(word_index[word])):
            out_str += " " + str(word_index[word][i])
        out_str += "\n"
        index_file.write(out_str)
    index_file.close()


if __name__ == '__main__':
    main()