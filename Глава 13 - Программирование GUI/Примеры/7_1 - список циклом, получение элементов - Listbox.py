import tkinter
import tkinter.messagebox

class ListboxExample:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.main_window, height=0, width=0, selectmode=tkinter.MULTIPLE)
        self.listbox.pack(padx=10, pady=10)

        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

        for day in days:
            self.listbox.insert(tkinter.END, day)

        self.get_button = tkinter.Button(self.main_window, text='Получить элемент', command=self.__retrieve_day)
        self.get_button.pack(padx=10, pady=5)

        tkinter.mainloop()

    def __retrieve_day(self):
        indexes = self.listbox.curselection()

        message = 'Выбранные элементы:\n'
        if indexes:
            for i in indexes:
                message += self.listbox.get(i) + '\n'
        else:
            message = 'Ни один элемент не выбран!'

        tkinter.messagebox.showinfo('Ваш выбор', message)


if __name__ == '__main__':
    listbox_example = ListboxExample()
