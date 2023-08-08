from objects import retail
from my_funcs import show_menu

DATA_FILE_NAME = r'data\stock.dat'

MAIN_MENU = {"1": "Меню продавца: ",
             "2": "Меню покупателя: ",
             "0": "Выход"}

SELLER_MENU = {"1": "Добавить товар",
               "2": "Редактировать товар",
               "3": "Показать остатки",
               "4": "Очистить склад",
               "0": "Вернуться назад"}

CUSTOMER_MENU = {"1": "Отобразить список доступных товаров",
                 "2": "Купить товар",
                 "3": "Посчитать стоимость покупок",
                 "4": "Показать корзину",
                 "5": "Очистить корзину",
                 "0": "Вернуться назад"}


def main():
    stock = retail.Stock()
    stock.load(DATA_FILE_NAME)
    while True:                             #MAIN MENU
        print("\nГЛАВНОЕ МЕНЮ")
        mm_choice = show_menu(MAIN_MENU)
        if mm_choice == "0":
            stock.save(DATA_FILE_NAME)
            print("\nbye, bye..\n")
            break

        elif mm_choice == "1":              # SELLER MENU
            while True:
                print("\nМЕНЮ ПРОДАВЦА")
                sm_choice = show_menu(SELLER_MENU)
                if sm_choice == "0":
                    break
                elif sm_choice == "1":      # Добавить товар
                    add_item_to_stock(stock)
                elif sm_choice == "2":      # Редактировать товар
                    modify_item_in_stock(stock)
                elif sm_choice == "3":      # Показать остатки
                    print("\nСОСТОЯНИЕ СКЛАДА: ")
                    stock.show()
                elif sm_choice == "4":      # Очистить склад
                    stock.clear()
                    print("\nСклад очищен..")

        elif mm_choice == "2":              # CUSTOMER MENU
            purchases = retail.CashRegister()
            while True:
                print("\nМЕНЮ ПОКУПАТЕЛЯ")
                cm_choice = show_menu(CUSTOMER_MENU)
                if cm_choice == "0":
                    break
                elif cm_choice == "1":      # Отобразить список доступных товаров
                    print()
                    stock.show()
                elif cm_choice == "2":      # Купить товар
                    buy_item(purchases, stock)
                elif cm_choice == "3":      # Посчитать стоимость покупок
                    print(f"\nОбщая стоимость покупок: {purchases.get_total():.2f} грн.")
                elif cm_choice == "4":      # Показать корзину
                    print("\nВаша корзина: ")
                    purchases.show_items()
                elif cm_choice == "5":      # Очистить корзину
                    purchases.clear(stock)
                    print("\nКорзина очищена..")


def add_item_to_stock(stock: retail.Stock):
    print("\nДОБАВЛЕНИЕ ТОВАРА НА СКЛАД")
    add_another = "Д"
    while add_another.upper() == "Д":
        item = retail.RetailItem()
        item.input_data()
        stock.add_item(item)
        add_another = ""
        while add_another.upper() not in ["Д", "Н"]:
            add_another = input("Добавить еще один товар? [Д/Н]: ")

def modify_item_in_stock(stock: retail.Stock):
    print("\nИЗМЕНЕНИЕ ТОВАРА НА СКЛАДЕ")
    descr = input("Введите наименование товара: ")
    item: retail.RetailItem = stock.get_item(descr)
    if item is not None:
        new_price = input("Введите новую цену (Enter - оставить без изменений): ")
        new_qty = input("Введите новое количество (Enter - оставить без изменений): ")
        if new_price.isdigit():
            item.set_price(float(new_price))
        if new_qty.isdigit():
            item.set_qty(int(new_qty))
        # stock.add_item(item)
    else:
        print(f"\nТовар {descr} на складе отсутствует")

def buy_item(purchases: retail.CashRegister, stock: retail.Stock):
    print("\nПОКУПКА. Выберите товар из списка: ")

    retail_menu = {str(key): val for key, val in enumerate(stock.get_items(), start=1)}
    # retail_menu = {}
    # for key, val in enumerate(stock.get_items(), start=1):
    #     retail_menu[str(key)] = val

    choice = show_menu(retail_menu)
    descr = retail_menu[choice]
    while True:
        qty = int(input("Укажите количество: "))
        if qty <= stock.get_item(descr).get_qty():
            price = stock.get_item(descr).get_price()
            item = retail.RetailItem(descr, qty, price)
            purchases.purchase_item(item)
            stock.update_qty(descr, -qty)
            break
        else:
            print("\nНеобходимого количества этого товара нет на складе!\n")


if __name__ == '__main__':
    main()