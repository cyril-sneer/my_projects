import tkinter
import tkinter.font
from tkinter.ttk import *

class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()

        self.picture_frame = Frame(self.root, padding=5, relief='groove')
        self.picture_frame.grid(padx=5, pady=5, sticky='NSEW', column=0, row=0)

        self.button_frame = Frame(self.root, padding=5, relief='groove', width=640)
        self.button_frame.grid(column=0, row=1, sticky='NSEW', padx=5, pady=5)

        Button(self.button_frame, text='Закрыть', command=self.root.destroy).\
            grid(column=0, row=0, sticky='sn', padx=10)

        self.canvas = tkinter.Canvas(self.picture_frame, width=700, height=500)
        self.canvas.grid(sticky='nsew')

        self.canvas.create_oval(150, 50, 550, 450)
        self.canvas.create_oval(180, 80, 520, 420)
        self.canvas.create_oval(210, 110, 490, 390)
        self.canvas.create_oval(240, 140, 460, 360)
        self.canvas.create_oval(270, 170, 430, 330)
        self.font = tkinter.font.Font(family='Calibri', size=14, weight='bold', slant='italic')
        self.canvas.create_text(350, 50, text='5', anchor='s', font=self.font)
        self.canvas.create_text(350, 80, text='4', anchor='s', font=self.font)
        self.canvas.create_text(350, 110, text='3', anchor='s', font=self.font)
        self.canvas.create_text(350, 140, text='2', anchor='s', font=self.font)
        self.canvas.create_text(350, 170, text='1', anchor='s', font=self.font)

        self.root.mainloop()


if __name__ == '__main__':
    gui = MyGUI()