#programmer = Caiden
#Date = 11.20.24
#Title = MPG


import tkinter
import tkinter.messagebox

class MPG:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.howManyMiles = tkinter.Label(self.top_frame, text = 'How many miles can your vehicle go on a full tank?')
        self.miles = tkinter.Entry(self.top_frame,width = 10 )
        self.gallons = tkinter.Label(self.middle_frame, text = 'How many gallons does your vehicle hold?')
        self.total_gallons = tkinter.Entry(self.middle_frame, width = 10)
        self.milesPerGallon = tkinter.Button(self.bottom_frame, text = 'MPG Calculation', command = self.mpg_Calc)
        self.quit = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)



        self.howManyMiles.pack()
        self.miles.pack()
        self.gallons.pack()
        self.total_gallons.pack()
        self.milesPerGallon.pack()
        self.quit.pack()
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()



    def mpg_Calc(self):
        milesStr = self.miles.get()
        gasStr = self.total_gallons.get()
        milesInt = int(milesStr)
        gasInt = int(gasStr)
        milesPerGallon = milesInt/gasInt
        tkinter.messagebox.showinfo('Miles Per Gallon', f'The MPG of your vehicle is {milesPerGallon}')
mpg = MPG()
