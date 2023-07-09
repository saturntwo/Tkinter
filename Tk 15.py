from tkinter import *

wind = Tk()
wind.title("Ввод-вывод данных")
wind.geometry("400x300")

def show():
    password = inputbox.get()
    bigl = 0
    smll = 0
    num = 0
    lent = True
    big = True
    sml = True
    nu = True
    fal = 0
    for i in range(len(password)):
        if password[i].isupper() == True: bigl+=1
        if password[i].isdigit() == True: num += 1
        if password[i].islower() == True: smll += 1
    if len(password)<6:
        lent = False
        fal+=1
    if bigl < 1:
        big = False
        fal += 1
    if smll < 1:
        sml = False
        fal += 1
    if num < 1:
        nu = False
        fal += 1

    if lent == False and fal == 1:
        label2.config(text='Пароль слишком короткий', fg='red')
    elif big == False and fal == 1:
        label2.config(text='Не хватает заглавных букв', fg='red')
    elif nu == False and fal == 1:
        label2.config(text='Не хватает цифр', fg='red')
    elif sml == False and fal == 1:
        label2.config(text='Не хватает строчных букв', fg='red')
    elif fal > 1:
        label2.config(text='Пароль не подходит', fg='red')
    else:
        label2.config(text='Пароль подходит', fg='green')

def theme():
    wind.config(bg='#353535')
    passwordbox.config(bg= '#353535', fg= 'white')
    label1.config(bg= '#353535', fg= 'white')
    label2.config(bg='#353535')
    showbutton.config(bg= '#535353', fg= 'white')
    themebutton.config(bg='#535353', fg='white', state = 'disabled')

passwordbox = LabelFrame(text = 'Проверка пароля')
label1 = Label(passwordbox, text = 'Введите пароль:')
showbutton = Button(passwordbox, text = 'Проверить пароль', width = 15, command= show)
inputbox = Entry(passwordbox, bg = 'black', fg = 'white',  justify=CENTER, width = 20, show='*')
label2 = Label(passwordbox, text = ' ', fg = 'black')
themebutton = Button(passwordbox, text = 'Сменить тему', width = 15, command= theme)


passwordbox.pack(pady = 40)
label1.pack(padx = 20, pady = 5)
inputbox.pack(padx = 20, pady = 5)
label2.pack(padx = 20, pady = 5)
showbutton.pack(padx = 20, pady = 5)
themebutton.pack(padx = 20, pady = 5)

wind.mainloop()