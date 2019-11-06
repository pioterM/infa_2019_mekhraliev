V = 20
A = 0.1
N = 0.9

from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
	def __init__(self, x, y):
		""" Конструктор класса ball
		Args:
		x - начальное положение мяча по горизонтали
		y - начальное положение мяча по вертикали
		"""
		self.x = x
		self.y = y
		self.r = 10
		self.vx = 0
		self.vy = 0
		self.color = choice(['blue', 'green', 'red', 'brown'])
		self.id = canv.create_oval(
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r,
				fill=self.color
		)
		self.live = 30

	def set_coords(self):
		canv.coords(
				self.id,
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r
		)

	def move(self):
		"""Переместить мяч по прошествии единицы времени.
		Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
		self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
		и стен по краям окна (размер окна 800х600).
		"""
		self.vy += A

		self.x += self.vx
		self.y += self.vy
		canv.move(self.id, self.vx, self.vy)

	def hittest(self, obj):
		"""Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
		Args:
			obj: Обьект, с которым проверяется столкновение.
		Returns:
			Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
		"""
		if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
			return True
		else:
			return False

	def walltest(self, wall1_x, wall1_y, wall2_x, wall2_y):
		res = True
		if self.x - self.r <= wall1_x and self.vx < 0:
			self.vx *= -1 * N
		elif self.x + self.r >= wall2_x and self.vx > 0:
			self.vx *= -1 * N
		if self.y - self.r <= wall1_y and self.vy < 0:
			self.vy *= -1 * N
		elif self.y + self.r >= wall2_y and self.vy > 0:
			self.vy *= -1 * N
		else:
			res = False
		return res



	def __del__(self):
		canv.delete(self.id)

class gun():
	def __init__(self):
		self.f2_power = 10
		self.f2_on = 0
		self.an = 1
		self.id = canv.create_line(20,450,50,420,width=7)

	def fire2_start(self, event):
		self.f2_on = 1

	def fire2_end(self, event):
		"""Выстрел мячом.
		Происходит при отпускании кнопки мыши.
		Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
		"""
		global balls, bullet
		bullet += 1
		new_ball = ball(self.xe, self.ye)
		new_ball.r += 5
		new_ball.vx = V / 100 * self.f2_power * math.cos(self.an)
		new_ball.vy = V / 100 * self.f2_power * math.sin(self.an)
		balls += [new_ball]
		self.f2_on = 0
		self.f2_power = 10

	def targetting(self, event=0):
		"""Прицеливание. Зависит от положения мыши."""
		if event:
			if (event.x-20) > 0:
				self.an = math.atan((event.y-450) / (event.x-20))
			elif (event.x-20) == 0:
				if (event.y-450) > 0:
					self.an = math.pi/2
				else:
					self.an = -math.pi / 2
			else:
				self.an = math.pi + math.atan((event.y - 450) / (event.x - 20))
		if self.f2_on:
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')

		self.xe = 20 + max(self.f2_power, 20) * math.cos(self.an)
		self.ye = 450 + max(self.f2_power, 20) * math.sin(self.an)
		canv.coords(self.id, 20, 450, self.xe, self.ye)

	def power_up(self):
		if self.f2_on:
			if self.f2_power < 100:
				self.f2_power += 1
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')


class target():
	points = 0
	id_points = canv.create_text(30, 30, text=points, font='28')

	def __init__(self):
		self.live = 1
		x = self.x = rnd(600, 780)
		y = self.y = rnd(300, 550)
		r = self.r = rnd(2, 50)
		color = self.color = 'red'
		self.id = canv.create_oval(x-r, y-r, x+r, y+r, fill=color)
		#target.id_points = canv.create_text(30,30,text = self.points,font = '28')
		canv.itemconfig(target.id_points,text = target.points,font = '28')

	def hit(self, points=1):
		"""Попадание шарика в цель."""
		canv.coords(self.id, -10, -10, -10, -10)
		target.points += points
		canv.itemconfig(self.id_points, text=self.points)

def new_game(event=''):
	global balls, bullet, sreen1, canv
	g1 = gun()
	bullet = 0
	t1 = target()
	balls = []
	canv.bind('<Button-1>', g1.fire2_start)
	canv.bind('<ButtonRelease-1>', g1.fire2_end)
	canv.bind('<Motion>', g1.targetting)

	canv.itemconfig(screen1, text='')
	t1.live = 1
	while t1.live or balls:
		for b in list(balls):
			b.move()
			if b.walltest(0,0, 800, 600) and abs(b.vy) <= A or not t1.live:
				balls.remove(b)
			if b.hittest(t1) and t1.live:
				t1.live = 0
				t1.hit()
				canv.bind('<Button-1>', '')
				canv.bind('<ButtonRelease-1>', '')
				if 10 <= bullet % 100 <= 20 or 5 <= bullet % 10 <= 9 or bullet % 10 == 0:
					shot = ' выстрелов'
				elif bullet % 10 == 1:
					shot = ' выстрел'
				else:
					shot = ' выстрела'
				canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + shot)
		canv.update()
		time.sleep(0.03)
		g1.targetting()
		g1.power_up()
	canv.delete(g1.id)
	root.after(2000, new_game)

screen1 = canv.create_text(400, 300, text='', font=('', 28))

new_game()

root.mainloop()
