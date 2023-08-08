import tkinter
from tkinter import ttk


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Расход топлива')

        self.data_frame = ttk.Frame(self.main_window, relief='ridge')
        self.data_frame.grid(padx=10, pady=10)

        ttk.Label(self.data_frame, text='Объем бензина в галлонах', width=25, justify='left'). \
            grid(column=0, row=0, padx=(10, 5))
        self.fuel_entry = ttk.Entry(self.data_frame, width=20)
        self.fuel_entry.grid(column=1, row=0, pady=(10, 5), padx=(5, 10))

        ttk.Label(self.data_frame, text='Дистанция в милях', width=25, justify='left'). \
            grid(column=0, row=1, padx=(10, 5))
        self.miles_entry = ttk.Entry(self.data_frame, width=20)
        self.miles_entry.grid(column=1, row=1, padx=(5, 10), pady=(5, 5))

        ttk.Label(self.data_frame, text='Расход миль/галлон', width=25, justify='left'). \
            grid(column=0, row=2, padx=(10, 5))
        self.value = tkinter.StringVar()
        ttk.Label(self.data_frame, width=20, textvariable=self.value). \
            grid(column=1, row=2, padx=(5, 10), pady=(5, 10))

        self.buttons_frame = ttk.Frame(self.main_window)
        self.buttons_frame.grid(padx=10, pady=(0, 10))

        ttk.Button(self.buttons_frame, text='Рассчитать', command=self.calc_fuel).grid(column=0, row=0)
        ttk.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy).grid(column=1, row=0)

        tkinter.mainloop()

    def calc_fuel(self):
        value = float(self.miles_entry.get()) / float(self.fuel_entry.get())
        self.value.set(f'{value:.2f}')


if __name__ == '__main__':
    my_gui = MyGUI()
