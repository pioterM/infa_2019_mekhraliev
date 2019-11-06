from tkinter import *

class LabelPlus(Label):
    def __init__(self, x, y)
        self.place(x,y)

    def place_by_Center(self, x, y):
        self.place(x, y)

root = Tk()
l1 = LabelPlus(root, bg='black', fg='white', width=20)
l1.place_by_Center(5, 5)
