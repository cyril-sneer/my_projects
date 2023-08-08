ALPHABET = " ,.?0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MORSE_LIST = [' ', '--..--', '.-.-.-', '..--..' ,'-----', '.----', '..---', '...--', '....-', '.....',
              '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.',
              '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
              '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']

MORSE_ALPHABET = dict(zip(ALPHABET, MORSE_LIST))
# MORSE_ALPHABET = dict()
# for i in range(len(ALPHABET)):
#     MORSE_ALPHABET[ALPHABET[i]] = MORSE_LIST[i]

input_string = input('Введите строку: ')
for ch in input_string:
    print(MORSE_ALPHABET[ch.upper()], end=' ')
print()

