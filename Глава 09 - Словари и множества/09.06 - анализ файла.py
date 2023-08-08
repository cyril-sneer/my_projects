FIRST_FILE_NAME = r'data\first_file.txt'
SECOND_FILE_NAME = r'data\second_file.txt'

first_file = open(FIRST_FILE_NAME, "r")
first_words_list = first_file.read().split()
first_file.close()
first_uniq_words_list = set(first_words_list)

second_file = open(SECOND_FILE_NAME, "r")
second_words_list = second_file.read().split()
second_file.close()
second_uniq_words_list = set(second_words_list)

all_words_in_both_files = first_uniq_words_list | second_uniq_words_list
print(f"Список всех уникальных слов, содержащихся в обоих файлах:\n {all_words_in_both_files}")

words_in_every_file = first_uniq_words_list & second_uniq_words_list
print(f"Cписок слов, входящих в оба файла:\n {words_in_every_file}")

words_in_first_not_in_second = first_uniq_words_list - second_uniq_words_list
print(f"Список слов из первого файла, не входящих во второй:\n {words_in_first_not_in_second}")

words_in_second_not_in_first = second_uniq_words_list - first_uniq_words_list
print(f"Список слов из второго файла, не входящих в первый:\n {words_in_second_not_in_first}")

words_in_one_file_only = first_uniq_words_list ^ second_uniq_words_list
print(f"Список слов, входящих либо в первый, либо во второй файл:\n {words_in_one_file_only}")
