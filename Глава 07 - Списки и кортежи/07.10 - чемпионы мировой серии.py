DATA_FILE_NAME = r'data\WorldSeriesWinners.txt'

def main():
    data_file= open(DATA_FILE_NAME, 'r')
    winners_list = [winner.rstrip() for winner in data_file.readlines()]
    data_file.close()

    sorted_unique_list = list(set(winners_list))
    sorted_unique_list.sort()
    for t in sorted_unique_list:
        print(t)

    team = input('\nВведите название комманды: ')
    t = winners_list.count(team)
    if t == 0:
        print('Эта команда ни разу не становилась чемпионом')
    else:
        print(f'Команда {team} становилась чемпионом {t} раз')


if __name__ == '__main__':
    main()