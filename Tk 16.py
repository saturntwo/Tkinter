from tkinter import *
from tkinter import filedialog

wind = Tk()
wind.title("Список дел")
wind.geometry("300x500")

k = 1
def add1():
    global k
    text = str(k) + '. ' + what.get() + '\t' + '(' + when.get() + ')' + '\n'
    todolist.insert(END, text)
    k+=1
    what.delete(0, END)
    when.delete(0, END)

def clear():
    todolist.delete(0.0, END)

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title = "Save file", filetypes = (("txt.files", "*.txt"),
                                                                      ("all files", "*.*")))
    if file:
        file.write(text)

def load():
    file = filedialog.askopenfile(title="Select file", filetypes=(("txt.files", "*.txt"),
                                                                  ("all files", "*.*")))
    text = file.read()
    todolist.insert(END, text)

main = LabelFrame(text = 'Записать важное дело')
label1 = Label(main, text = 'Какое дело')
label2 = Label(main, text = 'Когда нужно сделать')
what = Entry(main)
when = Entry(main)
add = Button(main, text = 'Добавить новое важное дело', command = add1)
todolist = Text(width = 33, height = 16)
delite = Button(text = 'Удалить все дела', command = clear)
saveb = Button(text = 'Сохранить', command = save)
loadb = Button(text = 'Загрузить', command = load)

main.pack(padx = 10, pady = 10)
label1.grid(row = 0, column = 0, padx = 5, pady = 5)
label2.grid(row = 0, column = 1, padx = 5, pady = 5)
what.grid(row = 1, column = 0, padx = 5, pady = 5)
when.grid(row = 1, column = 1, padx = 5, pady = 5)
add.grid(columnspan = 2, pady = 5)
todolist.pack()
delite.pack(pady = 5)
saveb.pack(pady = 5)
loadb.pack(pady = 5)


wind.mainloop()