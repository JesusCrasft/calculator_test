from tkinter import ttk
from tkinter import *


class Product:

    def __init__(self, window):

        # Windows Attributes
        self.wind = window
        self.wind.title('Calculator')
        self.wind.geometry("455x460")
        self.wind.resizable(False, False)

        #Variables
        self.operation = []
        self.ResP = 0
        self.ResPT = 0
        self.ResPI = 0
        self.ResD = 0

        # Treeview
        self.tree = ttk.Treeview(height=5, columns=2)
        self.tree.grid(row = 0, column = 0, sticky=W + E)
        self.tree.heading('#0', text = 'Operation', anchor=CENTER)
        self.tree.heading('#1', text = 'Result', anchor=CENTER)

        # Entry
        self.EntryOps = Entry(self.wind, font=('P052 35'), state='readonly', textvariable = self.operation)
        self.EntryOps.grid(row=4, column=0)

        # Buttons Space Bar
        self.barO = ttk.Button(self.wind).grid(row = 3, column = 0, sticky= W + E)
        self.barT = ttk.Button(self.wind).grid(row = 5, column = 0, sticky=W + E)
        
        
        # OPERATIONS BUTTONS

        # NUMBERS BUTTONS

        #Button nine
        self.nine = ttk.Button(text='9', width=10, command = lambda: self.printOps(9)).grid(row = 6, column = 0, sticky=E + E, padx=[0,190], ipady=10)
        
        #Button eight
        self.eight = ttk.Button(text='8', width=10, command = lambda: self.printOps(8)).grid(row = 6, column = 0, sticky=N + N, padx=[0,190], ipady=10)
        
        #Button seven
        self.seven = ttk.Button(text='7', width=10, command = lambda: self.printOps(7)).grid(row = 6, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        #Button six
        self.six = ttk.Button(text='6', width=10, command = lambda: self.printOps(6)).grid(row = 7, column = 0, sticky=E + E, padx=[0,190], ipady=10)

        #Button five
        self.five = ttk.Button(text='5', width=10, command = lambda: self.printOps(5)).grid(row = 7, column = 0, sticky=N + N, padx=[0,190], ipady=10)

        #Button four
        self.four = ttk.Button(text='4', width=10, command = lambda: self.printOps(4)).grid(row = 7, column = 0, sticky=W + W, padx=[0,220], ipady=10)
        
        #Button three
        self.three = ttk.Button(text='3', width=10, command = lambda: self.printOps(3)).grid(row = 8, column = 0, sticky=E + E, padx=[0,190], ipady=10)

        #Button two
        self.two = ttk.Button(text='2', width=10, command = lambda: self.printOps(2)).grid(row = 8, column = 0, sticky=N + N,  padx=[0,190], ipady=10)
        
        #Button one
        self.one = ttk.Button(text='1', width=10, command = lambda: self.printOps(1)).grid(row = 8, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        #Button zero
        self.zero = ttk.Button(text='0', width=10, command = lambda: self.printOps(0)).grid(row = 9, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        # SYMBOLS NUMBERS

        #=
        self.igual = ttk.Button(text='=', width=10, command = lambda: self.printRes()).grid(row = 9, column = 0, sticky=E + E, padx=[10,10], ipady=10)

        #DEL
        self.delBtn = ttk.Button(text='DEL', width=10, command = lambda: self.delEnt()).grid(row = 8, column = 0, sticky=E + E, padx=[10,10], ipady=10)

        #+
        self.suma = ttk.Button(text='+', width=10, command = lambda: self.printOps('+')).grid(row = 9, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #-
        self.resta = ttk.Button(text='-', width=10, command = lambda: self.printOps('-')).grid(row = 8, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #*
        self.multi = ttk.Button(text='x', width=10, command = lambda: self.printOps('*')).grid(row = 6, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #/
        self.slash = ttk.Button(text='/', width=10, command = lambda: self.printOps('/')).grid(row = 7, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #(
        self.pntsr = ttk.Button(text='(', width=10, command = lambda: self.printOps('(')).grid(row = 6, column = 0, sticky=E + E, padx=[0,10], ipady=10)
        
        #)
        self.pntsl = ttk.Button(text=')', width=10, command = lambda: self.printOps(')')).grid(row = 7, column = 0, sticky=E + E, padx=[0,10], ipady=10)

        #,
        self.coma = ttk.Button(text=',', width=10, command = lambda: self.printOps(',')).grid(row = 9, column = 0, sticky=N + N, padx=[0,190], ipady=10)

        #%
        self.porcentaje = ttk.Button(text='%', width=10, command = lambda: self.printOps('%')).grid(row = 9, column = 0, sticky=E + E, padx=[0,190], ipady=10)

    # Functions

    def printOps(self, number):
        
        self.EntryOps.configure(state='normal')
        self.EntryOps.delete(0, END)
        self.operation.append(number)
        self.EntryOps.insert(0, self.operation)
        self.EntryOps.configure(state='readonly')

    def delEnt(self):

        self.EntryOps.configure(state='normal')
        self.EntryOps.delete(self.EntryOps.index("end") - 1)
        self.operation = []
        self.EntryOps.configure(state='readonly')

    def printRes(self):

        # Print the operation into the Entry
 
        try: 
            self.ResPI = map(str, self.operation)
            self.ResPT = ''.join(self.ResPI)
            self.ResP = eval(self.ResPT)
            self.ResD = int(self.ResP)
            self.EntryOps.configure(state='normal')
            self.EntryOps.delete(0, END)
            self.EntryOps.insert(0, self.ResD)
            self.EntryOps.configure(state='readonly')
        except Exception as ex:
            self.EntryOps.configure(state='normal')
            self.EntryOps.delete(0, END)
            self.EntryOps.insert(0, 'Error')
            print(ex)
            self.EntryOps.configure(state='readonly')

        # Filling the tree with the operation + result

        
        

    



        

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()