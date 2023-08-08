import tkinter
import tkinter.messagebox
from tkinter.ttk import *

class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Междугородние звонки')

        self.frame = Frame(self.root, padding=(10, 5, 10, 5), relief='groove')
        self.frame.grid(padx=5, pady=5, sticky='NSEW')

        self.time_interval = tkinter.IntVar()
        self.time_interval.set(10)
        self.business_time_rb = Radiobutton(self.frame,
                                            text='Business time (6:00 - 17:49) - 10 грн/мин',
                                            variable=self.time_interval,
                                            value=10)
        self.prime_time_rb = Radiobutton(self.frame,
                                         text='Prime time (18:00 - 23:59) - 12 грн/мин',
                                         variable=self.time_interval,
                                         value=12)
        self.nonbusiness_time_rb = Radiobutton(self.frame,
                                               text='Non-business time (0:00 - 5:59) - 5 грн/мин',
                                               variable=self.time_interval,
                                               value=5)
        self.business_time_rb.grid(column=0, row=0, columnspan=2, sticky='wne')
        self.prime_time_rb.grid(column=0, row=1, columnspan=2, sticky='wne')
        self.nonbusiness_time_rb.grid(column=0, row=2, columnspan=2, sticky='wne')

        Label(self.frame, text='Продолжительность звонка').grid(column=0, row=3, sticky='wne')

        self.duration = tkinter.IntVar()
        self.duration.set(1)
        self.duration_spinbox = Spinbox(self.frame, from_=1, to=60, textvariable=self.duration, wrap=True, width=5)
        self.duration_spinbox.grid(column=1, row=3, sticky='wne')

        Button(self.frame, text='Рассчитать', command=self.calc).grid(column=0, row=5)
        Button(self.frame, text='Выйти', command=self.root.destroy).grid(column=1, row=5)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.root.mainloop()

    def calc(self):
        value = self.time_interval.get() * self.duration.get()
        tkinter.messagebox.showinfo(title='Стоимость звонка', message=f'{value} грн.')


if __name__ == '__main__':
    gui = MyGUI()