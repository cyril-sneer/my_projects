MONTHES = ["", "января", "февраля", "марта", "апреля", "мая", "июня",
           "июля", "августа", "сентября", "октября", "ноября", "декабря"]

def main():
    date_as_string = input("Введите дату в формате дд/мм/гггг: ")
    date_lst = date_as_string.split("/")
    day = int(date_lst[0])
    month = MONTHES[int(date_lst[1])]
    year = int(date_lst[2])
    print(f"Дата, которую вы ввели: {day} {month} {year} г.")

if __name__ == '__main__':
    main()