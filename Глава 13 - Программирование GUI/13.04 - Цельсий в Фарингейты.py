import tkinter
from tkinter import ttk


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Градусы Фарингейта')

        self.data_frame = ttk.Frame(self.main_window, relief='ridge')
        self.data_frame.grid(padx=10, pady=10)

        ttk.Label(self.data_frame, text='Градусы Цельсия', width=30, justify='left'). \
            grid(column=0, row=0, padx=(10, 5))
        self.celsius_entry = ttk.Entry(self.data_frame, width=20)
        self.celsius_entry.grid(column=1, row=0, pady=(10, 5), padx=(5, 10))

        ttk.Label(self.data_frame, text='Температура по Фаренгейту', width=30, justify='left'). \
            grid(column=0, row=1, padx=(10, 5))
        self.fahrenheit_value = tkinter.DoubleVar()
        ttk.Label(self.data_frame, width=20, textvariable=self.fahrenheit_value). \
            grid(column=1, row=1, padx=(5, 10), pady=(5, 10))

        self.buttons_frame = ttk.Frame(self.main_window)
        self.buttons_frame.grid(padx=10, pady=(0, 10))

        ttk.Button(self.buttons_frame, text='Рассчитать', command=self.fahrenheit). \
            grid(column=0, row=0, padx=5)
        ttk.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy). \
            grid(column=1, row=0, padx=5)

        tkinter.mainloop()

    def fahrenheit(self):
        value = (9 * float(self.celsius_entry.get())) / 5 + 32
        self.fahrenheit_value.set(value)


if __name__ == '__main__':
    my_gui = MyGUI()
