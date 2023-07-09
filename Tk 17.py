from tkinter import *
from random import randint
wind = Tk()
wind.title("tk")
wind.geometry("200x360")

global alarms

def generate_alarms():
    global alarmbox
    alarmbox.delete(0, END)
    alarms = []
    a = 0
    b = 20
    for m in range(3):
        if m == 1:
            a = 21
            b = 40
        elif m == 2:
            a = 41
            b = 59
        for i in range(3):
            last = str(randint(a, b))
            if int(last) < 10:
                text = '07:0' + str(last)
            else:
                text = '07:' + str(last)
            alarms.append(text)
    alarmbox.insert(END, *alarms)
    status.configure(text='Всего будильников: {}'.format(alarmbox.size()))

def delete_alarms():
    indexes = alarmbox.curselection()
    indexes = indexes[::-1]
    for i in indexes:
        alarmbox.delete(i)
    status.configure(text='Всего будильников: {}'.format(alarmbox.size()))

def open_change_window():
    global newalarm
    global alarms
    global newalarm
    global changewind
    changewind = Toplevel()
    changewind.title('Изменить')
    changewind.geometry('300x125')
    changewind.iconbitmap('alarm.ico')
    label3 = Label(changewind, text='Введите новое значение будильника')
    newalarm = Entry(changewind)
    newalarm.insert(0, alarmbox.get(ACTIVE))
    save = Button(changewind, text = 'Сохранить', width = 25,command= save_new_alarm)

    label3.pack(pady = 7)
    newalarm.pack(pady=7)
    save.pack(pady = 7)

def save_new_alarm():
    alarmbox.insert(ACTIVE, newalarm.get())
    alarmbox.delete(ACTIVE)
    changewind.destroy()

label1 = Label( text = 'Будильник')
alarmbox = Listbox(width = 30, height = 10, justify=CENTER, relief=GROOVE, bd=3, selectmode= EXTENDED)
status = Label()
random1 = Button(text = 'Случайные будильники', command= generate_alarms)
delete = Button(text = 'Удалить будильник', command = delete_alarms)
change = Button(text = 'Изменить будильник', command= open_change_window)

label1.pack(pady = 5)
status.pack(pady = 5)
alarmbox.pack(pady = 5)
random1.pack(pady = 5)
delete.pack(pady = 5)
change.pack(pady = 5)


wind.mainloop()