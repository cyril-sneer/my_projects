import tkinter
import tkinter.messagebox
from tkinter.ttk import *

class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Автоцех')

        self.check_box_frame = Frame(self.root, relief='groove')
        self.check_box_frame.grid(padx=10, pady=(10, 5))

        self.oil_change_price = 500.0
        self.oil_change_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text="замена масла - 500 грн",
                    variable=self.oil_change_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.lubrication_work_price = 300.0
        self.lubrication_work_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text="смазочные работы - 300 грн",
                    variable=self.lubrication_work_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.flushing_radiator_price = 700.0
        self.flushing_radiator_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text="промывка радиатора - 700 грн",
                    variable=self.flushing_radiator_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.transmission_fluid_change_price = 1000.0
        self.transmission_fluid_change_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text='замена трансмиссионной жидкости - 1000 грн',
                    variable=self.transmission_fluid_change_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.inspection_price = 800.0
        self.inspection_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text='осмотр - 800 грн',
                    variable=self.inspection_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.muffler_replacement_price = 1300.0
        self.muffler_replacement_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text='замена глушителя выхлопа - 1300 грн',
                    variable=self.muffler_replacement_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.tire_swapping_price = 1300.0
        self.tire_swapping_flag = tkinter.IntVar()
        Checkbutton(self.check_box_frame, text='перестановка шин - 1300 грн',
                    variable=self.tire_swapping_flag, command=self.calc).grid(sticky='w', pady=1, padx=1)

        self.total_frame = Frame(self.root)
        self.total_frame.grid(padx=10, pady=(5, 5))
        self.total_value = tkinter.DoubleVar()
        Label(self.total_frame, textvariable=self.total_value).grid()

        self.button_frame = Frame(self.root)
        self.button_frame.grid(padx=10, pady=(5, 10))
        Button(self.button_frame, text='Рассчитать', command=self.show_calculation).grid(column=0, row=0)
        Button(self.button_frame, text='Выход', command=self.root.destroy).grid(column=1, row=0)

        self.root.mainloop()

    def calc(self):
        total_value = self.oil_change_price * self.oil_change_flag.get() + \
                      self.lubrication_work_price * self.lubrication_work_flag.get() + \
                      self.flushing_radiator_price * self.flushing_radiator_flag.get() + \
                      self.transmission_fluid_change_price * self.transmission_fluid_change_flag.get() + \
                      self.inspection_price * self.inspection_flag.get() + \
                      self.muffler_replacement_price * self.muffler_replacement_flag.get() + \
                      self.tire_swapping_price * self.tire_swapping_flag.get()

        self.total_value.set(total_value)

    def show_calculation(self):
        self.calc()
        tkinter.messagebox.showinfo(title='Расчет',
                                    message=f'Общая стоимость работ\n{self.total_value.get()} грн.')

if __name__ == '__main__':
    gui = MyGUI()