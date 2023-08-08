ASSESSED_VALUE_PERCENT = 0.6
PROPERTY_TAX_RATE = 0.75 / 100

import tkinter
from tkinter.ttk import *


class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Расчет налога на недвижимость')

        self.data_frame = Frame(self.root)
        self.data_frame.grid(padx=10, pady=10)

        Label(self.data_frame, text='Фактическая стоимость имущества', justify='left', width=35).grid(column=0, row=0)
        self.fact_value_entry = Entry(self.data_frame)
        self.fact_value_entry.grid(column=1, row=0)

        Label(self.data_frame, text='Оценочная стоимость', justify='left', width=35).grid(column=0, row=1)
        self.assessed_value = tkinter.DoubleVar()
        self.assessed_value_label = Label(self.data_frame, textvariable=self.assessed_value)
        self.assessed_value_label.grid(column=1, row=1)

        Label(self.data_frame, text='Налог на недвижимость', justify='left', width=35).grid(column=0, row=2)
        self.property_tax = tkinter.DoubleVar()
        self.property_tax_label = Label(self.data_frame, textvariable=self.property_tax)
        self.property_tax_label.grid(column=1, row=2)

        self.buttons_frame = Frame(self.root)
        self.buttons_frame.grid(padx=10, pady=10)

        Button(self.buttons_frame, text='Рассчитать', command=self.calc).grid(column=0, row=0)
        Button(self.buttons_frame, text='Выйти', command=self.root.destroy).grid(column=1, row=0)

        self.root.mainloop()

    def calc(self):
        fact_value = self.fact_value_entry.get()
        if fact_value:
            fact_value = float(fact_value)
        else:
            fact_value = 0
        assessed_value = fact_value * ASSESSED_VALUE_PERCENT
        property_tax = assessed_value * PROPERTY_TAX_RATE
        self.assessed_value.set(assessed_value)
        self.property_tax.set(property_tax)


if __name__ == '__main__':
    gui = MyGUI()
