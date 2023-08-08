G = 9.8

def falling_distance(time):
    return (G * time ** 2) / 2

def main():
    print('-' * 26)
    for t in range(1, 11):
        print(f'| {t:5} c | {falling_distance(t):>10.2f} м |')
    print('-' * 26)

main()
