"""
This is GUI mod for Calc.py
"""
from tkinter import Button, Text, Tk, Frame, Entry
from Calc import *

# TODO It looks good on Ubuntu, but awful on Windows.
# it needs refactoring


class Calculator(Tk):
    def __init__(self):

        self.root = Tk()
        self.root.title('Calculator')

        self.display_log = Text()
        self.display_log.config(state='disabled',  width=35, height=10, cursor='arrow')
        self.display_log.pack()

        self.console = Entry(justify='right')
        self.console.pack(fill='x')

        self.make_numpad(self.root)
        self.make_operationpad(self.root)
        self.make_functionpad(self.root)
        self.root.mainloop()

    def make_numpad(self, master):
        # TODO construct pad from list
        self.numpad = Frame(master)
        self.numpad.pack(side='left')

        self.numpad9 = Frame(self.numpad)
        self.numpad9.pack()
        but_1 = Button(self.numpad9, text='1', command=lambda: self.insert_characters('1'))
        but_1.grid(row=0, column=0)

        but_2 = Button(self.numpad9, text='2', command=lambda: self.insert_characters('2'))
        but_2.grid(row=0, column=1)

        but_3 = Button(self.numpad9, text='3', command=lambda: self.insert_characters('3'))
        but_3.grid(row=0, column=2)

        but_4 = Button(self.numpad9, text='4', command=lambda: self.insert_characters('4'))
        but_4.grid(row=1, column=0)

        but_5 = Button(self.numpad9, text='5', command=lambda: self.insert_characters('5'))
        but_5.grid(row=1, column=1)

        but_6 = Button(self.numpad9, text='6', command=lambda: self.insert_characters('6'))
        but_6.grid(row=1, column=2)

        but_7 = Button(self.numpad9, text='7', command=lambda: self.insert_characters('7'))
        but_7.grid(row=2, column=0)

        but_8 = Button(self.numpad9, text='8', command=lambda: self.insert_characters('8'))
        but_8.grid(row=2, column=1)

        but_9 = Button(self.numpad9, text='9', command=lambda: self.insert_characters('9'))
        but_9.grid(row=2, column=2)

        self.numpad0 = Frame(self.numpad)
        self.numpad0.pack(fill='x')
        but_0 = Button(self.numpad0, text='0', command=lambda: self.insert_characters('0'))
        but_0.pack(fill='x')

    def make_operationpad(self, master, side=None):

        operationpad = Frame(master)
        operationpad.pack(side='left')

        but_plus = Button(operationpad, text='+', command=lambda: self.insert_characters('+'))
        but_plus.pack(fill='x')

        but_minus = Button(operationpad, text='-', command=lambda: self.insert_characters('-'))
        but_minus.pack(fill='x')

        but_mult = Button(operationpad, text='*', command=lambda: self.insert_characters('*'))
        but_mult.pack(fill='x')

        but_div = Button(operationpad, text='/', command=lambda: self.insert_characters('/'))
        but_div.pack(fill='x')

    def make_functionpad(self, master, side=None):

        functionpad = Frame(master)
        functionpad.pack(side='left')

        pad = Frame(functionpad)
        pad.pack()
        but_btk_lf = Button(pad, text='(', command=lambda: self.insert_characters('('))
        but_btk_lf.grid(row=0, column=0)

        but_btk_rg = Button(pad, text=')', command=lambda: self.insert_characters(')'))
        but_btk_rg.grid(row=0, column=1)

        but_sin = Button(pad, text='sin', command=lambda: self.insert_characters('sin('))
        but_sin.grid(row=1, column=0)

        but_cos = Button(pad, text='cos', command=lambda: self.insert_characters('cos('))
        but_cos.grid(row=1, column=1)

        but_tan = Button(pad, text='tan', command=lambda: self.insert_characters('tan('))
        but_tan.grid(row=2, column=0)

        but_log = Button(pad, text='log', command=lambda: self.insert_characters('log('))
        but_log.grid(row=2, column=1)

        # TODO make calculation at press Enter
        but_enter = Button(functionpad, text='=', command=lambda: self.parser(self.console.get()))
        but_enter.pack(fill='x')


    def insert_characters(self, character):
        self.index = len(self.console.get())
        self.console.insert(self.index, character)

    def parser(self, expression):
        # TODO correct output
        result = parser_expression(expression)
        self.display_log.config(state='normal')
        self.display_log.insert('insert', expression + '=' + result + '\n')
        self.display_log.config(state='disabled')
        self.console.delete(0, 100)
        self.console.insert(0, result)


calc = Calculator()
