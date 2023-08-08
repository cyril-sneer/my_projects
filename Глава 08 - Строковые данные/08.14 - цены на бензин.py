import copy
import matplotlib.pyplot as plt
import my_funcs


class Consts:
    # данные в файле хранятся с 5 апреля 1993 по 26 августа 2013 в формате MM-DD-YYYY:Price
    DATA_FILE_NAME = r"data\GasPrices.txt"
    MONTH = 0
    DAY = 1
    YEAR = 2
    PRICE = 3
    MENU = {"1": "Средняя цена за год",
            "2": "Средняя цена за месяц",
            "3": "Наибольшая и наименьшая цены в году",
            "4": "Цены по возрастанию",
            "5": "Цены по убыванию",
            "6": "Построить график",
            "0": "Выход"}


def read_data(file_name: str) -> list[list[int, int, int, float]]:
    data_file = open(file_name, 'r')
    data_as_strings = [string.rstrip() for string in data_file.readlines()]
    data_file.close()
    data_as_list = []
    for string in data_as_strings:
        data_as_list.append(str2list(string))
    return data_as_list


def str2list(data_string: str) -> list[int, int, int, float]:
    """
    Данные приходят в строке формата: "MM-DD-YYYY:Price"
    уходят в виде списка [MONTH, DAY, YEAR, PRICE]
    """
    price_record = [0, 0, 0, 0.0]
    date_and_price = data_string.split(":")
    price_record[Consts.MONTH], price_record[Consts.DAY], price_record[Consts.YEAR] = \
        map(int, date_and_price[0].split("-"))
    price_record[Consts.PRICE] = float(date_and_price[1])
    return price_record


def list2str(price_record: list[int, int, int, float]) -> str:
    """
    Данные приходят в виде списка [MONTH, DAY, YEAR, PRICE]
    уходят в строке формата: "MM-DD-YYYY:Price"
    """
    mm = str(price_record[Consts.MONTH])
    if len(mm) == 1: mm = "0" + mm
    dd = str(price_record[Consts.DAY])
    if len(dd) == 1: dd = "0" + dd
    yyyy = str(price_record[Consts.YEAR])
    price = f"{price_record[Consts.PRICE]:.3f}"
    data_string = mm + "-" + dd + "-" + yyyy + ":" + price
    return data_string


def input_integer(label: str, min_value: int, max_value: int) -> int:
    # input_ok = False
    while True:
        value_as_str = input(f"\nВведите {label} между {min_value} и {max_value}: ")
        if not value_as_str.isdigit():
            print("\nНекорректный ввод, повторите..")
        elif not (min_value <= int(value_as_str) <= max_value):
            print("\nНекорректный ввод, повторите..")
        else:
            return int(value_as_str)


def show_aver_for_year(data_array: list[list[int, int, int, float]]) -> None:
    yyyy = input_integer('год', 1993, 2013)
    year_sum = 0
    week_counter = 0
    for price_record in data_array:
        if price_record[Consts.YEAR] == yyyy:
            year_sum += price_record[Consts.PRICE]
            week_counter += 1
    aver_for_year = year_sum / week_counter
    print(f"\nСредняя цена топлива в {yyyy} году составила ${aver_for_year:.3f}\n")


def show_aver_for_month(data_array: list[list[int, int, int, float]]) -> None:
    yyyy = input_integer('год', 1993, 2013)
    if yyyy == 1993:
        mm = input_integer('месяц', 4, 12)
    elif yyyy == 2013:
        mm = input_integer('месяц', 1, 8)
    else:
        mm = input_integer('месяц', 1, 12)
    month_sum = 0
    week_counter = 0
    for price_record in data_array:
        if price_record[Consts.YEAR] == yyyy and price_record[Consts.MONTH] == mm:
            month_sum += price_record[Consts.PRICE]
            week_counter += 1
    aver_for_month = month_sum / week_counter
    print(f"\nСредняя цена в {mm} месяце {yyyy} года составила ${aver_for_month:.3f}\n")


def show_min_and_max_in_year(data_array: list[list[int, int, int, float]]) -> None:
    yyyy = input_integer('год', 1993, 2013)
    prices = [price_record[Consts.PRICE] for price_record in data_array if price_record[Consts.YEAR] == yyyy]
    print(f"\nНаименьшая цена в {yyyy} году составила ${min(prices):.3f}")
    print(f"Наибольшая цена в {yyyy} году составила ${max(prices):.3f}\n")


def prices_in_order(data_array: list[list[int, int, int, float]],
                    out_file_name: str,
                    reverse_order: bool = False) -> None:
    tmp_array = copy.copy(data_array)
    tmp_array.sort(key=lambda price_record: price_record[Consts.PRICE], reverse=reverse_order)
    out_file = open(out_file_name, 'w')
    for price_record in tmp_array:
        out_file.write(list2str(price_record) + "\n")
    out_file.close()
    print(f"\nДанные записаны в файл {out_file_name}\n")


def create_line_graph(data_array: list[list[int, int, int, float]]) -> None:
    # MM-DD-YYYY:Price
    x_array = []
    y_array = []
    x_tricks_pos = []
    x_tricks_labels = []
    yyyy = 1993
    new_year = True
    for price_record in data_array:
        x_array.append(list2str(price_record)[0:10])
        y_array.append(price_record[Consts.PRICE])
        if price_record[Consts.YEAR] > yyyy:
            yyyy = price_record[Consts.YEAR]
            new_year = True
        if new_year:
            x_tricks_pos.append(list2str(price_record)[0:10])
            x_tricks_labels.append(yyyy)
            new_year = False

    plt.plot(x_array, y_array)
    plt.title("График изменения цен на топливо с 04-1993 до 08-2013")
    plt.xlabel("Год")
    plt.ylabel("Цена, $")
    plt.xticks(x_tricks_pos, x_tricks_labels)
    plt.show()
    return


def main() -> None:
    data = read_data(Consts.DATA_FILE_NAME)
    while True:
        menu_choice = my_funcs.show_menu(Consts.MENU)
        if menu_choice == "0":
            print('\nbye, bye..')
            break
        elif menu_choice == "1":
            show_aver_for_year(data)
        elif menu_choice == "2":
            show_aver_for_month(data)
        elif menu_choice == "3":
            show_min_and_max_in_year(data)
        elif menu_choice == "4":
            prices_in_order(data, r"data\prices_in_ascending_order.txt", reverse_order=False)
        elif menu_choice == "5":
            prices_in_order(data, r"data\prices_in_descending_order.txt", reverse_order=True)
        elif menu_choice == "6":
            create_line_graph(data)


if __name__ == '__main__':
    main()
