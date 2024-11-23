#Programmer = Caiden Nelson
#Date = 11.21.24
#Title = Phone Call

import tkinter
import tkinter.messagebox

from tkinter import Radiobutton, Button, Entry, Label


class Phone:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        self.daytime_button = Radiobutton(self.top_frame, text = 'Daytime Rate',
                                          variable = self.radio_var, value = 1)
        self.evening_button = Radiobutton(self.top_frame, text = 'Evening Rate',
                                          variable = self.radio_var, value = 2)
        self.offpeak_button = Radiobutton(self.top_frame, text = 'Off-Peak Rate',
                                          variable = self.radio_var, value = 3)


        self.calculate_rate = Button(self.bottom_frame, text = 'Calculate Rata', command = self.rate)
        self.quit = Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)


        self.duration = Entry(self.middle_frame, width = 10)
        self.call_time = Label(self.middle_frame, text = 'How long is your call')



        self.daytime_button.pack()
        self.evening_button.pack()
        self.offpeak_button.pack()
        self.call_time.pack()
        self.duration.pack()
        self.calculate_rate.pack(side='left')
        self.quit.pack(side='left')
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()



    def rate(self):
        price = 0
        rate = self.radio_var.get()
        call_time = self.duration.get()
        int_call_time = int(call_time)
        if rate == 1:
            price = .02
        elif rate == 2:
            price = 0.12
        elif rate == 3:
            price = 0.05
        else:
            price = 0

        callrate = int_call_time*price
        tkinter.messagebox.showinfo('Price of Call', f'The price of your call is ${callrate}')
phone = Phone()
