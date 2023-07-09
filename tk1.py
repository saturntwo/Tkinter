from tkinter import *
# Настройки окна
wind = Tk()
wind.title("My program")
wind.geometry("400x250")
wind.maxsize(500,300)
wind.minsize(300,200)
wind.resizable(False, False)

# Виджеты
# имя виджета = Виджет(аргумент1 = значение1, аргумент2 = значение2б ...)
close = Button(text = 'Click me', width = 20, command = quit)
close.pack(expand = True)

# Конец программы
wind.mainloop()
