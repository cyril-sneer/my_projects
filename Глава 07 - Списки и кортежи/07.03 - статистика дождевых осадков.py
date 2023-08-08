import my_funcs

YEAR = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
MENU = {'1':'Ввод данных',
        '2':'Cуммарное количество',
        '3':'Среднее количество',
        '4':'Максимум',
        '5':'Минимум',
        '0':'Выход'}

def main():
    fallout = []
    while True:
        choice = my_funcs.show_menu(MENU)
        if choice == '0':
            print('\nbye, bye..')
            break
        elif choice == '1': # Ввод данных
            for month in YEAR:
                _data = float(input(f'Input data for {month}: '))
                fallout.append(_data)
            print()
        else:
            if len(fallout) == 0: print('\nPlease, input data first..\n')
            elif choice == '2': # Cуммарное количество
                _sum = sum(fallout)
                print(f'\nTotal - {_sum:.1f}\n')
            elif choice == '3': # Среднее количество
                _aver = sum(fallout)/len(fallout)
                print(f'\nAverage - {_aver:.1f}\n')
            elif choice == '4': # Максимум
                _max = max(fallout)
                max_month_index = fallout.index(_max)
                max_month_name = YEAR[max_month_index]
                print(f'\n Max fallout level is {_max} in {max_month_name}\n')
            elif choice == '5': # Минимум
                _min = min(fallout)
                min_month_index = fallout.index(_min)
                min_month_name = YEAR[min_month_index]
                print(f'\nMin fallout level is {_min} in {min_month_name}\n')



if __name__ == '__main__':
    main()