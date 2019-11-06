from tkinter import *

root = Tk()
root.title("GUI на Python")
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 200
root.geometry('400x400+{}+{}'.format(w, h))

#задание вспомогательных классов для добавления нужных методов
#функция располагающая элемент относительно центра элемента
class LabelPlus(Label):
    def place_by_Center(self, x, y):
        window_size_X=root.winfo_width() # ширина окна
        window_size_Y=root.winfo_height() # высота окна

        if type(x)=='str':
            x = int('0'+x)
            x = window_size_X*x - self['width']//2
        else:
            x -= self['width']//2
        if type(y)=='str':
            y = int('0'+x)
            y = window_size_Y*y - self['height']//2
        else:
            x -= self['height']//2
        self.place(x, y)

#задание объектов в окне
e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l1 = LabelPlus(root, bg='black', fg='white', width=20)
l2 = LabelPlus(root, bg='black', fg='white', width=20, text='Python 3')
e.place(x=115, y=200)

l1.place_by_Center(5, 5)

#функция по выводу введенных слов по алфавиту
def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l1['text'] = ' '.join(s)
    l1['width'] = 30
    l1['bg'] = "grey90"
    l1['fg'] = "grey24"
    w = root.winfo_screenwidth()//2 - 250
    h = root.winfo_screenheight()//2 - 250
    root.geometry("500x500+{}+{}".format(w, h))
    l1['font'] = "Times New Roman", 14
    l1.place_by_Center(.5, .5)




b.bind('<Button-1>', strToSortlist)

l2.pack()
e.pack()
b.pack()
l1.pack()


root.mainloop()
