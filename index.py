from tkinter import ttk
from tkinter import *


class Product:

    def __init__(self, window):

        # Windows Attributes
        self.wind = window
        self.wind.title('Calculator')
        self.wind.geometry("860x620")
        #self.wind.geometry("455x460")
        self.wind.resizable(False, False)

        # VARIABLES
        self.YesPr = True
        self.operation = []
        self.TkStyle = ttk.Style()
        self.ResP = 0
        self.ResPT = 0
        self.ResPI = 0
        self.ResD = 0
        
        # TREEVIEW
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=0, column=0, sticky = E + E)
        #self.TkStyle.configure('Treeview', rowheight=10)
        #self.TkStyle.theme_use('clam')

        #Operation Colum
        self.tree.heading('#0', text = 'Operation', anchor = CENTER)
        self.tree.column('#0', width=430)

        #Result Colum
        self.tree.heading('#1', text = 'Result', anchor = CENTER)
        self.tree.column('#1', width=430)

        # Entry
        self.EntryOps = Entry(self.wind, font=('P052 35'), width=37 , textvariable = self.operation)
        self.EntryOps.grid(row=4, column=0)

        # BUTTONS SPACE BAR
        #Up Bar
        self.barO = ttk.Button(self.wind).grid(row=3, column=0, sticky= W + E)
        #Down Bar
        self.barT = ttk.Button(self.wind).grid(row=5, column=0, sticky=W + E)
        
        
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

        # SYMBOLS BUTTONS

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

        #÷
        self.division = ttk.Button(text='÷', width=10, command = lambda: self.printOps('/')).grid(row = 7, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #(
        self.pntsr = ttk.Button(text='(', width=10, command = lambda: self.printOps('(')).grid(row = 6, column = 0, sticky=E + E, padx=[0,10], ipady=10)
        
        #)
        self.pntsl = ttk.Button(text=')', width=10, command = lambda: self.printOps(')')).grid(row = 7, column = 0, sticky=E + E, padx=[0,10], ipady=10)

        #,
        self.coma = ttk.Button(text=',', width=10, command = lambda: self.printOps(',')).grid(row = 9, column = 0, sticky=N + N, padx=[0,190], ipady=10)

        #%
        self.porcentaje = ttk.Button(text='%', width=10, command = lambda: self.printOps('%')).grid(row = 9, column = 0, sticky=E + E, padx=[0,190], ipady=10)

    # Functions

    #Function to print the operation in the Entry
    def printOps(self, number):

        if self.YesPr == True:
            self.EntryOps.delete(0, END)
            self.operation.append(number)
            self.EntryOps.insert(0, self.operation)
        

    #Function to delete all the caracters in the Entry
    def delEnt(self):
        self.EntryOps.configure(state='normal')
        #self.EntryOps.delete(self.EntryOps.index("end") - 1)
        self.EntryOps.delete(0, END)
        self.operation = []
        self.YesPr = True

    # Print the result into the Entry and the TreeView
    def printRes(self):

        if self.YesPr == True:
            if self.operation == []:
                self.EntryOps.delete(0, END)
                self.EntryOps.insert(0, "Error, presione DEL")
                self.tree.insert('', 0, text = "Error", values = ["Operacion en blanco"])
                self.operation = []
                self.YesPr = False
                self.EntryOps.configure(state='readonly')
            
            else:
                try: 
                    self.ResPI = map(str, self.operation)
                    self.ResPT = ''.join(self.ResPI)
                    self.ResP = eval(self.ResPT)
                    self.ResD = int(self.ResP)
                    self.EntryOps.delete(0, END)
                    self.EntryOps.insert(0, self.ResD)
                    self.tree.insert('', 0, text = self.operation, values = self.ResD)
                    self.operation = []

                except ZeroDivisionError:
                    self.EntryOps.delete(0, END)
                    self.EntryOps.insert(0, 'Error, presione DEL')
                    self.tree.insert('', 0, text = self.operation, values = ["Error al intentar dividir entre cero"])
                    self.operation = []
                    self.YesPr = False
                    self.EntryOps.configure(state='readonly')

                except SyntaxError:
                    self.EntryOps.delete(0, END)
                    self.EntryOps.insert(0, 'Error, presione DEL')
                    self.tree.insert('', 0, text = self.operation, values = ["Operacion invalida"])
                    self.operation = []
                    self.YesPr = False
                    self.EntryOps.configure(state='readonly')

        
        
        

    



        

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()