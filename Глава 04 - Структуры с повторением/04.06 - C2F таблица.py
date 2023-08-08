def fahrenheit(celsius: int):
    return (9 * celsius) / 5 + 32

print(f'C\tF')
print('-' * 10)

for c in range(21):
    print(f'{c}\t{fahrenheit(c):.2f}')
