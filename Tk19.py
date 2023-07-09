from tkinter import *
wind = Tk()
wind.title("Color picker")
wind.geometry("550x300")

def color_generate(value):
    red = scale_R.get()
    green = scale_G.get()
    blue = scale_B.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    label_color.config(bg=color, text = color)

frame_RGB = LabelFrame(height = 250, width = 250, text = 'Выберите цвета')
frame_color = LabelFrame(height = 250, width = 250, text = 'Полученный цвет')
label_color = Label(frame_color, height = 8, width = 16, font =('Arial', 15, 'bold'))
scale_R = Scale(frame_RGB, from_ = 0, to = 255, resolution = 1, orient = HORIZONTAL,
                label = 'Красный', length = 200, width = 20, fg = "red", activebackground= "red", command=)
scale_G = Scale(frame_RGB, from_ = 0, to = 255, resolution = 1, orient = HORIZONTAL,
                label = 'Зелёный', length = 200, width = 20, fg = "green", activebackground= "green")
scale_B = Scale(frame_RGB, from_ = 0, to = 255, resolution = 1, orient = HORIZONTAL,
                label = 'Синий', length = 200, width = 20, fg = "blue", activebackground= "blue")


frame_RGB.place(relx = 0.03, rely = 0.07)
frame_color.place(relx = 0.52, rely = 0.07)
label_color.place(relx = 0.1, rely = 0.06)
scale_R.place(relx = 0.05, rely = 0.05)
scale_G.place(relx = 0.05, rely = 0.35)
scale_B.place(relx = 0.05, rely = 0.65)
wind.mainloop()