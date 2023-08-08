import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Преобразование км в мили')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text='Введите расстояние в километрах: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text='Преобразовано в мили: ')

        # Объект StringVar нужен для того, чтобы его связать
        # с выходной надписью. Для сохранения последовательности
        # пробелов используется метод set данного объекта.
        self.value = tkinter.StringVar()

        # Создать надпись Label и связать ее с объектом StringVar.
        # Любые значения, хранящиеся в объекте StringVar,
        # будут автоматически выводиться в надписи Label.
        self.miles_label = tkinter.Label(self. mid_frame, textvariable=self.value)

        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Преобразовать', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Выйти', command=self.main_window.destroy)

        self.calc_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        self.top_frame.pack(padx=5, pady=5)
        self.mid_frame.pack(padx=5, pady=5)
        self.bottom_frame.pack(padx=5, pady=5)

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(f'{miles:.2f}')
        tkinter.messagebox.showinfo(title='Результат',
                                    message=f'{kilo:.2f} километров эквивалентно {miles:.2f} миль')


if __name__ == '__main__':
    my_gui = MyGUI()