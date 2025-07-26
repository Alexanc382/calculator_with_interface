from tkinter import *
from tkinter import ttk
import calculator_logic as c

oper = ''
first = 0
second = 0

def calc():
    try:
        second = float(entry.get())
        result = None
        if oper == '+':
            result = c.add(first, second)
        elif oper == '-':
            result = c.subtraction(first, second)
        elif oper == '*':
            result = c.multiply(first, second)
        elif oper == '/':
            result = c.divide(first, second)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, 'На ноль делить нельзя')

def enter_number(number):
    entry.insert(END, number)

def clear_entry():
    entry.delete(0, END)

def set_operation(operation):
    global first
    global oper
    first = float(entry.get())
    oper = operation
    entry.delete(0, END)


def set_exponen_2(first):
    first = float(entry.get())
    entry.delete(0, END)
    result_ex_2 = c.square(first)
    entry.insert(0, str(result_ex_2))


def set_exponen_3(first):
    first = float(entry.get())
    entry.delete(0, END)
    result_ex_3 = c.cube(first)
    entry.insert(0, str(result_ex_3))

def validate_entry():
    e = entry.get()
    txt = ''.join(b for b in e if b in '0123456789.-')
    if e != txt:
        entry.delete(0, END)
        entry.insert(0, txt)


window = Tk()
window.title('Калькулятор')
style = ttk.Style()
style.configure('numbers.TButton', background='#FFC0C0') # цифры
style.configure('arithmetic_oper.TButton', background='#DDA0DD') # арифм. действия
style.configure('С.TButton', background='#FF69B4') # кнопка "С"
style.configure('equals.TButton', background='#FF00FF') # "равно"

entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=3, sticky='ew') #растянули на три столбца
entry.bind('<KeyRelease>',lambda event: validate_entry())

ttk.Button(text='1', command=lambda: enter_number('1'), style='numbers.TButton').grid(row=1, column=0)
ttk.Button(text='2', command=lambda: enter_number('2'), style='numbers.TButton').grid(row=1, column=1)
ttk.Button(text='3', command=lambda: enter_number('3'), style='numbers.TButton').grid(row=1, column=2)
ttk.Button(text='4', command=lambda: enter_number('4'), style='numbers.TButton').grid(row=2, column=0)
ttk.Button(text='5', command=lambda: enter_number('5'), style='numbers.TButton').grid(row=2, column=1)
ttk.Button(text='6', command=lambda: enter_number('6'), style='numbers.TButton').grid(row=2, column=2)
ttk.Button(text='7', command=lambda: enter_number('7'), style='numbers.TButton').grid(row=3, column=0)
ttk.Button(text='8', command=lambda: enter_number('8'), style='numbers.TButton').grid(row=3, column=1)
ttk.Button(text='9', command=lambda: enter_number('9'), style='numbers.TButton').grid(row=3, column=2)
ttk.Button(text='0', command=lambda: enter_number('0'), style='numbers.TButton').grid(row=4, column=0)

ttk.Button(text='+', command=lambda: set_operation('+'), style='arithmetic_oper.TButton').grid(row=4, column=1)
ttk.Button(text='-', command=lambda: set_operation('-'), style='arithmetic_oper.TButton').grid(row=4, column=2)
ttk.Button(text='*', command=lambda: set_operation('*'), style='arithmetic_oper.TButton').grid(row=5, column=0)
ttk.Button(text='/', command=lambda: set_operation('/'), style='arithmetic_oper.TButton').grid(row=5, column=1)
ttk.Button(text='x²', command=lambda: set_exponen_2('first'), style='arithmetic_oper.TButton').grid(row=5, column=2)
ttk.Button(text='x³', command=lambda: set_exponen_3('first'), style='arithmetic_oper.TButton').grid(row=6, column=0)

ttk.Button(text='C', command=clear_entry, style='С.TButton').grid(row=6, column=1)
ttk.Button(text='=', command=calc, style='equals.TButton').grid(row=6, column=2)



window.mainloop()