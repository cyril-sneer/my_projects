import tkinter
from tkinter import ttk

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Персональная информация')

        self.info_frame = ttk.Frame(self.main_window)
        self.button_frame = ttk.Frame(self.main_window)

        self.address = tkinter.StringVar()
        self.address_label = ttk.Label(self.info_frame, textvariable=self.address)
        self.address_label.pack()

        self.info_button = ttk.Button(self.button_frame, text='Показать инфо', command=self.show_info)
        self.quit_button = ttk.Button(self.button_frame, text='Выйти', command=self.main_window.destroy)
        self.info_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        self.info_frame.pack(padx=20, pady=10)
        self.button_frame.pack(padx=20, pady=10)

        tkinter.mainloop()
    def show_info(self):
        self.address.set('просп. Гагарина, 41-А/52,\nХарьков, UA')


if __name__ == '__main__':
    my_gui = MyGUI()