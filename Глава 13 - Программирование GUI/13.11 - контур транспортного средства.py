import tkinter
import tkinter.font
from tkinter.ttk import *

class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()

        self.picture_frame = Frame(self.root, padding=5, relief='groove')
        self.picture_frame.grid(padx=5, pady=5, sticky='NSEW', column=0, row=0)

        self.button_frame = Frame(self.root, padding=5, relief='groove')
        self.button_frame.grid(column=0, row=1, sticky='NSEW', padx=5, pady=5)

        Button(self.button_frame, text='Закрыть', command=self.root.destroy).\
            grid(sticky='ew')

        self.canvas = tkinter.Canvas(self.picture_frame, width=600, height=400)
        self.canvas.grid(sticky='nsew')

        self.canvas.create_rectangle(50, 100, 400, 300, fill='grey')
        self.canvas.create_polygon(400, 150, 500, 150, 550, 200, 550, 300, 400, 300, 400, 150,
                                   fill='green', outline='black')
        self.canvas.create_polygon(410, 160, 490, 160, 535, 205, 535, 220, 410, 220, 410, 160,
                                   fill='lightblue', outline='black')

        self.canvas.create_oval(75, 300, 150, 375, fill='black')
        self.canvas.create_oval(95, 320, 130, 355, fill='blue')

        self.canvas.create_oval(160, 300, 235, 375, fill='black')
        self.canvas.create_oval(180, 320, 215, 355, fill='red')

        self.canvas.create_oval(440, 300, 515, 375, fill='black')
        self.canvas.create_oval(460, 320, 495, 355, fill='silver')

        self.font = tkinter.font.Font(family='Arial', size=74, weight='bold', slant='roman')
        self.canvas.create_text(225, 200, text='ХЛЕБ', anchor='center', font=self.font)

        self.root.mainloop()


if __name__ == '__main__':
    gui = MyGUI()