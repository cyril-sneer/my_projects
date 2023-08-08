DATA_FILE_NAME = r'data\USPopulation.txt'
BASE_YEAR = 1950

def main():
    min_year = 0
    max_year = 0
    min_delta = 0
    max_delta = 0

    data_file = open(DATA_FILE_NAME, 'r')
    data = [float(year.rstrip()) for year in data_file.readlines()]
    data_file.close()

    for year in range(1, len(data)):
        delta = data[year] - data[year - 1]

        if year == 1:
            min_year = year
            max_year = year
            min_delta = delta
            max_delta = delta
        else:
            if delta < min_delta:
                min_delta = delta
                min_year = year
            if delta > max_delta:
                max_delta = delta
                max_year = year

    aver_per_year = (data[-1] - data[0]) / (len(data) - 1)

    print(f'Средний прирост населения с 1950 по 1990 гг составил {aver_per_year:.1f} тыс человек в год')
    print(f'Наименьший прирост был в {min_year + BASE_YEAR}, он составил {min_delta:.1f} тыс человек в год')
    print(f'Наибольший прирост был в {max_year + BASE_YEAR}, он составил {max_delta:.1f} тыс человек в год')


if __name__ == '__main__':
    main()