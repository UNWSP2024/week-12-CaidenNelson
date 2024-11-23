#Programmer = Caiden Nelson
#Date = 11.20.24
#Title = Car Repair

import tkinter
import tkinter.messagebox



class Repair:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)



        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        self.var5 = tkinter.IntVar()
        self.var6 = tkinter.IntVar()
        self.var7 = tkinter.IntVar()

        self.oilChange = tkinter.Checkbutton(self.top_frame, text = 'Oil Change',
                                             variable =self.var1, onvalue = 1, offvalue = 0)
        self.lubeJob = tkinter.Checkbutton(self.top_frame, text = 'Lube Job',
                                           variable =self.var2, onvalue = 1, offvalue = 0)
        self.radiatorFlush = tkinter.Checkbutton(self.top_frame, text = 'Radiator Flush',
                                                 variable =self.var3, onvalue = 1, offvalue = 0)
        self.transmissionFluid = tkinter.Checkbutton(self.top_frame, text = 'Transmission Fluid',
                                                     variable =self.var4, onvalue = 1, offvalue = 0)
        self.inspection = tkinter.Checkbutton(self.top_frame, text = 'Inspection',
                                              variable =self.var5, onvalue = 1, offvalue = 0)
        self.mufflerReplacement = tkinter.Checkbutton(self.top_frame, text = 'Muffler Replacement',
                                                      variable =self.var6, onvalue = 1, offvalue = 0)
        self.tireRotation = tkinter.Checkbutton(self.top_frame, text = 'Tire Rotation',
                                                variable =self.var7, onvalue = 1, offvalue = 0)
        self.totalPrice = tkinter.Button(self.bottom_frame, text = 'Total Price', command = self.find_price)
        self.quit = tkinter.Button(self.bottom_frame,text = 'Quit', command = self.main_window.destroy)



        self.oilChange.pack()
        self.lubeJob.pack()
        self.radiatorFlush.pack()
        self.transmissionFluid.pack()
        self.inspection.pack()
        self.mufflerReplacement.pack()
        self.tireRotation.pack()


        self.totalPrice.pack()
        self.quit.pack()


        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def find_price(self):



        oilChangePrice=0
        lubeJobPrice=0
        radiatorFlushPrice=0
        transmissionFluidPrice=0
        inspectionPrice=0
        mufflerReplacementPrice=0
        tireRotationPrice=0



        oilChange = self.var1.get()
        lubeJob = self.var2.get()
        radiatorFlush = self.var3.get()
        transmissionFluid = self.var4.get()
        inspection = self.var5.get()
        mufflerReplacement = self.var6.get()
        tireRotation = self.var7.get()

        if oilChange == 1:
            oilChangePrice = 30
        else:
            oilChangePrice = oilChangePrice
        if lubeJob == 1:
            lubeJobPrice = 20
        else:
            lubeJobPrice = lubeJobPrice
        if radiatorFlush == 1:
            radiatorFlushPrice = 40
        else:
            radiatorFlushPrice = radiatorFlushPrice
        if transmissionFluid == 1:
            transmissionFluidPrice = 100
        else:
            transmissionFluidPrice = transmissionFluidPrice
        if inspection == 1:
            inspectionPrice = 35
        else:
            inspectionPrice = inspectionPrice
        if mufflerReplacement == 1:
            mufflerReplacementPrice = 200
        else:
            mufflerReplacementPrice = mufflerReplacementPrice
        if tireRotation == 1:
            tireRotationPrice = 20
        else:
            tireRotationPrice = tireRotationPrice
        total_price = (oilChangePrice + lubeJobPrice + radiatorFlushPrice
                       + tireRotationPrice + transmissionFluidPrice
                       + inspectionPrice + mufflerReplacementPrice)
        tkinter.messagebox.showinfo('Total Price', f'The total price is {total_price}$')



repair = Repair()

