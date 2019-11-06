from tkinter import *
from random import randrange as rnd, choice
import math
import time

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = randint(0,5)
        deltay = randint(0,5)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

# initialize root Window and canvas
root = Tk()
#задает размер окна и его расположение на экране (по центру)
w = root.winfo_screenwidth()//2 - 400
h = root.winfo_screenheight()//2 - 300
root.geometry("800x600+{}+{}".format(w, h))
flag = 0
#задание переменных для подсчета и объектов для отображения счета очков
count = 0
x1 = y1 = r1 = 0
cou = Label(root, font=("Comic Sans MS", 24, "bold"))
cou.place(x = .5,y = .5)
cou['text'] = count

cou.pack()
#создание холста
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)



# create two ball objects and animate them
x = rnd(100,700) #выбор рандомных значений шарика
y = rnd(100,500)
r = rnd(30,50)
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

ball1.move_ball()
ball2.move_ball()

root.mainloop()
