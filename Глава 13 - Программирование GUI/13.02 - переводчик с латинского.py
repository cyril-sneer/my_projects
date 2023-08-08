import tkinter
from tkinter import ttk

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Переводчик с латинского')

        self.translation_frame = ttk.Frame(self.main_window)
        self.button_frame = ttk.Frame(self.main_window)

        self.translation = tkinter.StringVar()
        self.translation_label = ttk.Label(self.translation_frame, textvariable=self.translation)
        self.translation_label.pack()

        self.first_button = ttk.Button(self.button_frame, text='sinister', command=self.translate_1)
        self.second_button = ttk.Button(self.button_frame, text='dexter', command=self.translate_2)
        self.third_button = ttk.Button(self.button_frame, text='medium', command=self.translate_3)
        self.first_button.pack(side='left')
        self.second_button.pack(side='left')
        self.third_button.pack(side='left')

        self.translation_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    # def translate(self, word):
    #     if word == 'sinister':
    #         self.translation.set('Левый')
    #     elif word == 'dexter':
    #         self.translation.set('Правый')
    #     elif word == 'medium':
    #         self.translation.set('Центральный')

    def translate_1(self):
        self.translation.set('Левый')
    def translate_2(self):
        self.translation.set('Правый')
    def translate_3(self):
        self.translation.set('Центральный')


if __name__ == '__main__':
    my_gui = MyGUI()