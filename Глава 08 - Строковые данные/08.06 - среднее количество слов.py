INPUT_FILE_NAME = r"data\text.txt"

input_file = open(INPUT_FILE_NAME, 'r')
sentences = [string.rstrip() for string in input_file.readlines()]
input_file.close()

# sentences_by_words = [sent.split() for sent in sentences]
# words_quantity = list(map(len, sentences_by_words))
# average_words = sum(words_quantity)/len(words_quantity)

num_sentences = len(sentences)
total_words = 0
for item in sentences:
    words = item.split()
    total_words += len(words)

average_words = total_words/num_sentences

print(f'Average words quantity = {average_words:.0f}')