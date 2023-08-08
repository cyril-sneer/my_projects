import pickle

class RetailItem:
    def __init__(self, description: str = "", qty: int = 0, price: float = 0.00):
        self.__descr = description
        self.__qty = qty
        self.__price = price

    def set_descr(self, description):
        self.__descr = description
    def get_descr(self):
        return self.__descr

    def set_qty(self, quantity):
        self.__qty = quantity
    def get_qty(self):
        return self.__qty

    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

    def input_data(self):
        self.set_descr(input("Введите описание товара: "))
        self.set_price(float(input("Введите цену единицы в грн: ")))
        self.set_qty(int(input("Введите количество единиц: ")))

    def __str__(self):
        result = f'Товар: {self.__descr}\t' \
                 f'Цена: {self.__price:.2f} грн.\t' \
                 f'Количество: {self.__qty}'
        return result


class Stock:
    def __init__(self):
        self.__items = {}

    def load(self, data_file: str):
        try:
            file = open(data_file, 'rb')
            self.__items = pickle.load(file)
            file.close()
        except IOError:
            self.__items = {}

    def save(self, data_file: str):
        file = open(data_file, 'wb')
        pickle.dump(self.__items, file)
        file.close()

    def show(self):
        for item in self.__items:
            print(self.__items[item])

    def clear(self):
        self.__items = {}

    def add_item(self, item: RetailItem):
        self.__items[item.get_descr()] = item

    def get_items(self):
        return self.__items

    def get_item(self, descr: str):
        return self.__items.get(descr, None)

    def update_qty(self, descr, delta):
        qty = self.__items[descr].get_qty()
        self.__items[descr].set_qty(qty + delta)


class CashRegister:
    def __init__(self):
        self.__purchase_list = []

    def purchase_item(self, item: RetailItem):
        self.__purchase_list.append(item)

    def get_total(self):
        total = 0
        for item in self.__purchase_list:
            total += item.get_qty() * item.get_price()
        return total

    def show_items(self):
        for item in self.__purchase_list:
            print(item)

    def clear(self, stock:Stock):
        for item in self.__purchase_list:
            stock.update_qty(item.get_descr(), item.get_qty())
        self.__purchase_list = []