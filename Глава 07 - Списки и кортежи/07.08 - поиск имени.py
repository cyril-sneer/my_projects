GIRL_NAMES_FILE = r'data\GirlNames.txt'
BOY_NAMES_FILE = r'data\BoyNames.txt'

def main():
    girl_names_file = open(GIRL_NAMES_FILE, 'r')
    girl_names_list = [name.rstrip() for name in girl_names_file.readlines()]
    girl_names_file.close()

    girl_name = input('Введите женское имя: ')

    if girl_name != '':
        if girl_name in girl_names_list: print('Женское имя относится к частым!\n')
        else: print('Это редкое женское имя!')
    else: print('Вы не ввели женское имя!\n')


    boy_names_file = open(BOY_NAMES_FILE, 'r')
    boy_names_list = [name.rstrip() for name in boy_names_file.readlines()]
    boy_names_file.close()

    boy_name = input('Введите мужское имя: ')

    if boy_name != '':
        if boy_name in boy_names_list: print('Мужское имя относится к частым!\n')
        else: print('Это редкое мужское имя!\n')
    else: print('Вы не ввели мужское имя!')

if __name__ == '__main__':
    main()



