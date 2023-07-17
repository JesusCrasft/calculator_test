from tkinter import ttk
from tkinter import *


class Product:


        

    #def operations(self, number):

        #self.operation = number
        #self.result.insert(0, self.operation)

    def __init__(self, window):

        # Windows Attributes
        self.wind = window
        self.wind.title('Calculator')
        self.wind.geometry("455x460")
        self.wind.resizable(False, False)

        # Creating Frame Container
        #result = Frame(self.wind, height=120, width=460, relief='solid').grid(row=0, column=0, columnspan = 3)
        #self.buttons = Frame(self.wind,height=150, width=150, relief='solid').grid(row=6, column=0)
        

        # Buttons Space Bar
        self.barO = ttk.Button(self.wind).grid(row = 3, column = 0, sticky= W + E)
        self.barT = ttk.Button(self.wind).grid(row = 5, column = 0, sticky=W + E)
        
        
        # OPERATIONS BUTTONS

        # NUMBERS BUTTONS

        #Button nine
        self.nine = ttk.Button(text='9', width=10).grid(row = 6, column = 0, sticky=E + E, padx=[0,190], ipady=10)
        
        #Button eight
        self.eight = ttk.Button(text='8', width=10).grid(row = 6, column = 0, sticky=N + N, padx=[0,190], ipady=10)
        
        #Button seven
        self.seven = ttk.Button(text='7', width=10, command = lambda: self.operatio(7)).grid(row = 6, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        #Button six
        self.six = ttk.Button(text='6', width=10).grid(row = 7, column = 0, sticky=E + E, padx=[0,190], ipady=10)

        #Button five
        self.five = ttk.Button(text='5', width=10).grid(row = 7, column = 0, sticky=N + N, padx=[0,190], ipady=10)

        #Button four
        self.four = ttk.Button(text='4', width=10).grid(row = 7, column = 0, sticky=W + W, padx=[0,220], ipady=10)
        
        #Button three
        self.three = ttk.Button(text='3', width=10).grid(row = 8, column = 0, sticky=E + E, padx=[0,190], ipady=10)

        #Button two
        self.two = ttk.Button(text='2', width=10).grid(row = 8, column = 0, sticky=N + N,  padx=[0,190], ipady=10)
        
        #Button one
        self.one = ttk.Button(text='1', width=10).grid(row = 8, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        #Button zero
        self.zero = ttk.Button(text='0', width=10).grid(row = 9, column = 0, sticky=W + W, padx=[0,220], ipady=10)

        # SYMBOLS NUMBERS

        #=
        self.igual = ttk.Button(text='=', width=10).grid(row = 9, column = 0, sticky=E + E, padx=[10,10], ipady=10)

        #+
        self.suma = ttk.Button(text='+', width=10).grid(row = 9, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #-
        self.resta = ttk.Button(text='-', width=10).grid(row = 8, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #*
        self.multi = ttk.Button(text='x', width=10).grid(row = 6, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #/
        self.slash = ttk.Button(text='/', width=10).grid(row = 7, column = 0, sticky=E + E, padx=[0,100], ipady=10)

        #(
        self.pntsr = ttk.Button(text='(', width=10).grid(row = 6, column = 0, sticky=E + E, padx=[0,10], ipady=10)
        
        #)
        self.pntsl = ttk.Button(text=')', width=10).grid(row = 7, column = 0, sticky=E + E, padx=[0,10], ipady=10)

        #,
        self.coma = ttk.Button(text=',', width=10).grid(row = 9, column = 0, sticky=N + N, padx=[0,190], ipady=10)

        #%
        self.porcentaje = ttk.Button(text='%', width=10).grid(row = 9, column = 0, sticky=E + E, padx=[0,190], ipady=10)
    
        self.operation = 0
        self.result = []


        # Entrys
        self.Eresult = Entry(self.wind, font=('P052 35'), state='readonly', textvariable = self.operation)
        self.Eresult.grid(row=4, column=0)


        # Treeview
        self.tree = ttk.Treeview(height=5, columns=2)
        self.tree.grid(row = 0, column = 0, sticky=W + E)
        self.tree.heading('#0', text = 'Operation', anchor=CENTER)
        self.tree.heading('#1', text = 'Result', anchor=CENTER)

        # Functions

    def operatio(self, number):
        
        self.operation = number
        self.result = self.operation
        self.Eresult = Entry(self.wind, font=('P052 35'), state='readonly', textvariable = StringVar(value = self.operation))
        self.Eresult.grid(row=4, column=0)
        print(self.result)



      

        

    


        

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()