from tkinter import ttk
from tkinter import * 

class Product:

    def __init__(self, window):
        
        #+++++++++++++++++++
        # Windows Attributes
        #+++++++++++++++++++

        self.wind = window
        self.wind.title('Calculator')
        self.wind.geometry("860x620")
        self.wind.resizable(False, False)


        #++++++++++
        # VARIABLES
        #++++++++++

        self.YesPr = False
        self.NoPr = True
        self.operation = []
        self.old_operation = []
        self.TkStyle = ttk.Style()
        self.ResP = 0
        self.ResPT = 0
        self.ResPI = 0
        self.ResD = 0

        
        #+++++++++++
        # SCROLLBARS
        #+++++++++++

        #Treeview Scrollbar
        self.barO = Scrollbar(self.wind, orient='horizontal', width=30)
        self.barO.grid(row=3, column=0, sticky = W + E)

        #Entry Scrollbar
        self.barT = Scrollbar(self.wind, orient='horizontal', width=30)
        self.barT.grid(row=5, column=0, sticky = W + E)


        #+++++++++
        # TREEVIEW
        #+++++++++

        self.tree = ttk.Treeview(height=10, columns=2, yscrollcommand=self.barO.set)
        self.tree.grid(row=0, column=0, sticky = E + E)
        self.TkStyle.configure('Treeview', font=('courier 20'))
        self.TkStyle.configure('Treeview.Heading', font=('P052 15'))

        #Operation Colum
        self.tree.heading('#0', text = 'OPERATIONS', anchor = CENTER)
        self.tree.column('#0', width=430, stretch=False)

        #Result Colum
        self.tree.heading('#1', text = 'RESULT', anchor = CENTER)
        self.tree.column('#1', width=430, stretch=False)


        #++++++
        # ENTRY
        #++++++

        self.EntryOps = Entry(self.wind, state='readonly', xscrollcommand=self.barT.set, font=('P052 35'), width=37 , textvariable = self.operation)
        self.EntryOps.grid(row=4, column=0)


        # Scrollbars Configuration
        self.barT.configure(command=self.EntryOps.xview) 
        self.barO.configure(command=self.tree.yview)
        

        #+++++++++++++++++++
        # OPERATIONS BUTTONS
        #+++++++++++++++++++
        
        #++++++++++++++++
        # NUMBERS BUTTONS
        #++++++++++++++++

        #Button nine
        self.nine = ttk.Button(text='9', width=20, command = lambda: self.printOps(9))
        self.nine.grid(row = 6, column = 0, sticky=E + E, padx=[0,350], ipady=10)
        
        #Button eight
        self.eight = ttk.Button(text='8', width=20, command = lambda: self.printOps(8))
        self.eight.grid(row = 6, column = 0, sticky=N + N, padx=[0,350], ipady=10)
        
        #Button seven
        self.seven = ttk.Button(text='7', width=20, command = lambda: self.printOps(7))
        self.seven.grid(row = 6, column = 0, sticky=W + W, padx=[0,0], ipady=10)

        #Button six
        self.six = ttk.Button(text='6', width=20, command = lambda: self.printOps(6))
        self.six.grid(row = 7, column = 0, sticky=E + E, padx=[0,350], ipady=10)

        #Button five
        self.five = ttk.Button(text='5', width=20, command = lambda: self.printOps(5))
        self.five.grid(row = 7, column = 0, sticky=N + N, padx=[0,350], ipady=10)

        #Button four
        self.four = ttk.Button(text='4', width=20, command = lambda: self.printOps(4))
        self.four.grid(row = 7, column = 0, sticky=W + W, padx=[0,0], ipady=10)
        
        #Button three
        self.three = ttk.Button(text='3', width=20, command = lambda: self.printOps(3))
        self.three.grid(row = 8, column = 0, sticky=N + N, padx=[0,7], ipady=10)

        #Button two
        self.two = ttk.Button(text='2', width=20, command = lambda: self.printOps(2))
        self.two.grid(row = 8, column = 0, sticky=N + N,  padx=[0,350], ipady=10)
        
        #Button one
        self.one = ttk.Button(text='1', width=20, command = lambda: self.printOps(1))
        self.one.grid(row = 8, column = 0, sticky=N + N, padx=[0,690], ipady=10)

        #Button zero
        self.zero = ttk.Button(text='0', width=20, command = lambda: self.printOps(0))
        self.zero.grid(row = 8, column = 0, sticky=S + S, padx=[0,690], ipady=10)


        #++++++++++++++++
        # SYMBOLS BUTTONS
        #++++++++++++++++

        #Equal
        self.equal = ttk.Button(text='=', width=21, command = lambda: self.printRes())
        self.equal.grid(row = 8, column = 0, sticky=E + E, padx=[0,0], ipady=35)

        #Del All
        self.delAll = ttk.Button(text='DEL ALL', width=55, command = lambda: self.delAEnt())
        self.delAll.grid(row = 9, column = 0, sticky=W + W, padx=[0,0], ipady=10)

        #Del
        self.delBtn = ttk.Button(text='DEL', width=55, command = lambda: self.delEnt())
        self.delBtn.grid(row = 9, column = 0, sticky=E + E, padx=[0,0], ipady=10)

        #Plus
        self.plus = ttk.Button(text='+', width=20, command = lambda: self.printOps('+'))
        self.plus.grid(row = 8, column = 0, sticky=S + S, padx=[338,0], ipady=10)

        #Minus
        self.minus = ttk.Button(text='-', width=20, command = lambda: self.printOps('-'))
        self.minus.grid(row = 8, column = 0, sticky=N + N, padx=[338,0], ipady=10)

        #Multi
        self.multi = ttk.Button(text='x', width=20, command = lambda: self.printOps('*'))
        self.multi.grid(row = 6, column = 0, sticky=E + E, padx=[0,177], ipady=10)

        #Division
        self.division = ttk.Button(text='÷', width=20, command = lambda: self.printOps('/'))
        self.division.grid(row = 7, column = 0, sticky=E + E, padx=[0,177], ipady=10)

        #pntsr
        self.pntsr = ttk.Button(text='(', width=20, command = lambda: self.printOps('('))
        self.pntsr.grid(row = 6, column = 0, sticky=E + E, padx=[0,5], ipady=10)
        
        #pntsl
        self.pntsl = ttk.Button(text=')', width=20, command = lambda: self.printOps(')'))
        self.pntsl.grid(row = 7, column = 0, sticky=E + E, padx=[0,5], ipady=10)

        #Comma
        self.comma = ttk.Button(text=',', width=20, command = lambda: self.printOps(','))
        self.comma.grid(row = 8, column = 0, sticky=S + S,  padx=[0,350], ipady=10)

        #Percent
        self.percent = ttk.Button(text='%', width=20, command = lambda: self.printOps('%'))
        self.percent.grid(row = 8, column = 0, sticky=S + S, padx=[0,7], ipady=10)


    #+++++++++
    # FUNCTIONS
    #+++++++++

    #Function to print the operation in the Entry
    def printOps(self, number):
            if self.NoPr == True:
                self.operation.append(number)
                self.old_operation = self.operation
                self.ResPI = map(str, self.operation)
                self.ResPT = ''.join(self.ResPI)
                self.operation = self.ResPT
                self.YesPr = True
                self.EntryOps.configure(state='normal')
                self.EntryOps.delete(0, END)
                self.EntryOps.insert(0, self.operation)
                self.EntryOps.configure(state='readonly')
                self.operation = self.old_operation


    #Functions to delete only one caracter in the Entry
    def delEnt(self):
        if self.YesPr == True:
            try:
                self.EntryOps.configure(state='normal')
                self.EntryOps.delete(self.EntryOps.index("end") - 1)
                self.EntryOps.configure(state='readonly')
                self.operation.pop()

            except IndexError:
                print("kuru kuru kururin")    
        

    #Functions to delete all the caracters in the Entry
    def delAEnt(self):
        self.EntryOps.configure(state='normal')
        self.EntryOps.delete(0, END)
        self.EntryOps.configure(state='readonly')
        self.operation = []
        self.YesPr = False
        self.NoPr = True


    #Function to print the result into the Entry and the TreeView
    def printRes(self):
        if self.YesPr == True:
            try: 
                self.ResPI = map(str, self.operation)
                self.ResPT = ''.join(self.ResPI)
                self.operation = self.ResPT
                self.ResP = eval(self.ResPT)
                self.EntryOps.configure(state='normal')
                self.EntryOps.delete(0, END)
                self.EntryOps.insert(0, self.ResP)
                self.tree.insert('', 0, text = self.operation, values = self.ResP)
                self.EntryOps.configure(state='readonly')
                self.operation = []
                self.YesPr = False

            except ZeroDivisionError:
                self.EntryOps.configure(state='normal')
                self.EntryOps.delete(0, END)
                self.EntryOps.insert(0, 'Error: Press DEL ALL to continue')
                self.operation = self.ResPT
                self.tree.insert('', 0, text = self.operation, values = ["Error: Division by zero"])
                self.operation = []
                self.YesPr = False
                self.NoPr = False
                self.EntryOps.configure(state='readonly')

            except SyntaxError:
                self.EntryOps.configure(state='normal')
                self.EntryOps.delete(0, END)
                self.EntryOps.insert(0, 'Error: Press DEL ALL to continue')
                self.operation = self.ResPT
                self.tree.insert('', 0, text = self.operation, values = ["Error: Invalid Operation"])
                self.operation = []
                self.YesPr = False
                self.NoPr = False
                self.EntryOps.configure(state='readonly')

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()