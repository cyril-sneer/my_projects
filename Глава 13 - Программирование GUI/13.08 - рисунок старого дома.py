import tkinter
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

        self.canvas.create_rectangle(150, 250, 550, 450, fill='orange')
        self.canvas.create_rectangle(320, 350, 380, 450, fill='brown')
        self.canvas.create_rectangle(200, 300, 275, 375, fill='blue')
        self.canvas.create_rectangle(420, 300, 495, 375, fill='lightblue')
        self.canvas.create_polygon(150, 250, 100, 250, 350, 100, 600, 250, 150, 250, fill='magenta')
        self.canvas.create_oval(550, 20, 650, 120, outline='yellow', fill='yellow')


        self.root.mainloop()


if __name__ == '__main__':
    gui = MyGUI()