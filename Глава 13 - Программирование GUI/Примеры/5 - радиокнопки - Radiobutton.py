import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window, borderwidth=1, relief='raised')
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать объект IntVar для использования с виджетами Radiobutton.
        self.radio_var = tkinter.IntVar()
        # Назначить объекту IntVar значение 1
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Вариант 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Вариант 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Вариант 3', variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Выход', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack(padx=20, pady=20)
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Выбор', f'Выбран вариант {self.radio_var.get()}')


if __name__ == '__main__':
    my_gui = MyGUI()
