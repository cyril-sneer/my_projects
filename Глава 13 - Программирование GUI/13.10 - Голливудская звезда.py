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

        self.canvas = tkinter.Canvas(self.picture_frame, width=800, height=700)
        self.canvas.grid(sticky='nsew')

        """
        self.canvas.create_polygon(400, 100,
                                   500, 300,
                                   700, 300,
                                   530, 400,
                                   600, 600,
                                   400, 500,
                                   200, 600,
                                   270, 400,
                                   100, 300,
                                   300, 300,
                                   400, 100,
                                   fill='',
                                   outline='black') """

        self.canvas.create_polygon(400, 100, 600, 650, 100, 300, 700, 300, 200, 650,
                                   fill='gold', outline='gold')

        self.font = tkinter.font.Font(family='Calibri', size=34, weight='bold', slant='italic')
        self.canvas.create_text(400, 370, text='Sergey', anchor='center', font=self.font)

        self.root.mainloop()


if __name__ == '__main__':
    gui = MyGUI()