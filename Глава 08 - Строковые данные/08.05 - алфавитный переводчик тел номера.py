TEL_DICT = dict(A = 2, B = 2, C = 2,
                D = 3, E = 3, F = 3,
                G = 4, H = 4, I = 4,
                J = 5, K = 5, L = 5,
                M = 6, N = 6, O = 6,
                P = 7, Q = 7, R = 7, S = 7,
                T = 8, U = 8, V = 8,
                W = 9, X = 9, Y = 9, Z = 9)

input_tel_number = input("Input tel number in XXX-XXX-XXXX format: ")
input_tel_number = input_tel_number.upper()
converted_tel_number = ""

for ch in input_tel_number:
    if ch.isalpha():
        converted_tel_number += str(TEL_DICT[ch])
    else:
        converted_tel_number += ch

print(f"Converted tel number is: {converted_tel_number}")
