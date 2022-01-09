from tkinter import *
import iconwindow

# funciones

i = 0


def click(valor):
    global i
    pantalla.insert(i, valor)
    i += 1


def borrar():
    # global i
    pantalla.delete(0, END)
    # i = 0


def calcular():
    entrada = pantalla.get()
    salida = eval(entrada)
    pantalla.delete(0, END)
    pantalla.insert(0, salida)


root = Tk()

root.title('CALCULADORA')
root.resizable(1, 1)
iconwindow.iconwindow(root, 'ico-logo')

    
miFrame = Frame(root)

root.config(bd='8')
pantalla = Entry()
pantalla.config(width=16, font='Arial 16')
pantalla.grid(column=0, row=0, padx=2, pady=2, columnspan=4)

bt_del = Button(text='Del', width=2, height=2, command=borrar)
bt_par1 = Button(text='(', width=2, height=2, command=lambda:click('('))
bt_par2 = Button(text=')', width=2, height=2, command=lambda:click(')'))
bt_div = Button(text='/', width=2, height=2, command=lambda:click('/'))

bt_del.grid(row=1, column=0)
bt_par1.grid(row=1, column=1)
bt_par2.grid(row=1, column=2)
bt_div.grid(row=1, column=3)

bt_7 = Button(text='7', width=2, height=2, command=lambda:click(7))
bt_8 = Button(text='8', width=2, height=2, command=lambda:click(8))
bt_9 = Button(text='9', width=2, height=2, command=lambda:click(9))
bt_mul = Button(text='*', width=2, height=2, command=lambda:click('*'))

bt_7.grid(row=2, column=0)
bt_8.grid(row=2, column=1)
bt_9.grid(row=2, column=2)
bt_mul.grid(row=2, column=3)

bt_4 = Button(text='4', width=2, height=2, command=lambda:click(4))
bt_5 = Button(text='5', width=2, height=2, command=lambda:click(5))
bt_6 = Button(text='6', width=2, height=2, command=lambda:click(6))
bt_sum = Button(text='+', width=2, height=2, command=lambda:click("+"))

bt_4.grid(row=3, column=0)
bt_5.grid(row=3, column=1)
bt_6.grid(row=3, column=2)
bt_sum.grid(row=3, column=3)

bt_1 = Button(text='1', width=2, height=2, command=lambda:click(1))
bt_2 = Button(text='2', width=2, height=2, command=lambda:click(2))
bt_3 = Button(text='3', width=2, height=2, command=lambda:click(3))
bt_res = Button(text='-', width=2, height=2, command=lambda:click('-'))

bt_1.grid(row=4, column=0)
bt_2.grid(row=4, column=1)
bt_3.grid(row=4, column=2)
bt_res.grid(row=4, column=3)

bt_0 = Button(text='0', width=8, height=2, command=lambda:click(0))
bt_pun = Button(text='.', width=2, height=2, command=lambda:click('.'))
bt_igual = Button(text='=', width=2, height=2, command=calcular)

bt_0.grid(row=5, column=0, columnspan=2)
bt_pun.grid(row=5, column=2)
bt_igual.grid(row=5, column=3)

root.mainloop()
