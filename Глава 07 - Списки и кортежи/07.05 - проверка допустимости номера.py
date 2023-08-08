IN_FILE_NAME: str = r'data\charge_accounts.txt'

def main():
    in_file = open(IN_FILE_NAME, 'r')
    accounts_list: list[str] = [acc.rstrip() for acc in in_file.readlines()]
    in_file.close()

    account = input('Введите номер счета: ')
    if account in accounts_list:
        print('Номер счета допустим!')
    else:
        print('Номер счета не найден!')


if __name__ == '__main__':
    main()