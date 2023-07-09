from tkinter import *

wind = Tk()
wind.title("Позиционирование виджетов")
wind.geometry("400x250")
wind.resizable(False, False)
label1 = Label(text = ' gsrligvjnswu gsinugrn uinghuihrui nhughi\n'
                      ' nuh nvhsgigigi hin irhgu hnurig\n'
                      'shreug dgbxhrht hhbr\n'
                      'gdgbrtgde', justify=CENTER, relief=RIDGE, bd=5, bg='black', fg = 'white',
                        font='Comic 8 bold', width=50, height=5 )
label1.grid(column=0, row=0, columnspan=2, rowspan=1, padx=10,  pady=10)
button1 = Button(text = 'Button 1', bg = 'red', fg = 'white', activebackground='blue', activeforeground='yellow', width = 15)
button2 = Button(text = 'Button 2', bg = 'green', fg = 'white',  activebackground='blue', activeforeground='yellow', width = 15)
button1.place(x=20, y=110)
button2.place(x=245, y=110)
frame1 = Frame()
frame2 = Frame()


wind.mainloop()