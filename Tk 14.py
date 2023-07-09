from tkinter import *

wind = Tk()
wind.title("Ввод-вывод данных")
wind.geometry("400x300")

def show():
    outputbox.delete(0, END)
    password = inputbox.get()
    outputbox.insert(END, password)


passwordbox = LabelFrame(text = 'Пароль')
label1 = Label(passwordbox, text = 'Введите пароль:')
label2 = Label(passwordbox, text = 'Ваш пароль:')
showbutton = Button(passwordbox, text = 'Показать', width = 15, command = show)
inputbox = Entry(passwordbox, bg = 'black', fg = 'white',  justify=CENTER, width = 20, show='*')
outputbox = Entry(passwordbox, justify=CENTER, width = 20)

passwordbox.pack(pady = 40)
label1.pack(padx = 20, pady = 5)
inputbox.pack(padx = 20, pady = 5)
label2.pack(padx = 20, pady = 5)
outputbox.pack(padx = 20, pady = 5)
showbutton.pack(padx = 20, pady = 5)

wind.mainloop()