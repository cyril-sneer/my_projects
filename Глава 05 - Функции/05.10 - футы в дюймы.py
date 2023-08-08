def feet_to_inches(feets):
    return feets * 12

def main():
    feets = float(input('Введите количество футов:\t'))
    inches = feet_to_inches(feets)

    print(f'{feets:.2f} футов = {inches:.2f} дюймов')


main()