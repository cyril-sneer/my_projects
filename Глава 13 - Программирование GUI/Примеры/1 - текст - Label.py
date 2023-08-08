import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Мой первый GUI")

        # Создание надписи
        self.label1 = tkinter.Label(self.main_window,  # корневой виджет
                                    text="Привет, мир!",  # собственно надпись
                                    borderwidth=1,  # толщина линии вокруг
                                    relief='groove')  # тип линии вокруг
        self.label2 = tkinter.Label(self.main_window,  # корневой виджет
                                    text="Это моя программа с GUI.",  # собственно надпись
                                    borderwidth=1,  # толщина линии вокруг
                                    relief='ridge')  # тип линии вокруг

        self.label1.pack(ipadx=20, ipady=20, padx=20, pady=20)  # внутреннее и внешнее заполнение
        self.label2.pack(ipadx=20, ipady=20, padx=(10, 5), pady=(20, 10))  # внутреннее и внешнее заполнение

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()