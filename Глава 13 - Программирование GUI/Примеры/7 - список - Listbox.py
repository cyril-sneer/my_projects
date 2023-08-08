import tkinter

class ListboxExample:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.main_window, height=7, width=0)
        self.listbox.pack(padx=10, pady=10)

        self.listbox.insert(0, "Понедельник")
        self.listbox.insert(1, "Вторник")
        self.listbox.insert(2, "Среда")
        self.listbox.insert(3, "Четверг")
        self.listbox.insert(4, "Пятница")
        self.listbox.insert(5, "Суббота")
        self.listbox.insert(6, "Воскресенье")

        tkinter.mainloop()

if __name__ == '__main__':
    listbox_example = ListboxExample()
