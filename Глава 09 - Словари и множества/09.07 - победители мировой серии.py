DATA_FILE_NAME = r"data\WorldSeriesWinners.txt"

def main():
    input_file = open(DATA_FILE_NAME, 'r')
    teams = [line.rstrip() for line in input_file.readlines()]
    input_file.close()

    wins_counter = {}
    winners_by_year = {}

    y = 1903
    for team in teams:
        wins_counter.setdefault(team, 0)
        wins_counter[team] += 1
        # if team not in wins_counter:
        #     wins_counter[team] =1
        # else:
        #     wins_counter[team] += 1
        winners_by_year[y] = team
        y += 1

    while True:
        year_str = input("Введите год между 1903 и 2008: ")
        if not year_str.isdigit():
            print("Некорректный ввод, повторите..")
        elif not (1903 <= int(year_str) <= 2008):
            print("Некорректный ввод, повторите..")
        else:
            year = int(year_str)
            winner = winners_by_year[year]
            break

    if year == 1904 or year == 1993:
        print(winner)
    else:
        print(f"В {year} году победителем мировой серии стала команда {winner}")
        print(f"Всего команда {winner} одержала {wins_counter[winner]} побед в мировой серии")


if __name__ == '__main__':
    main()
