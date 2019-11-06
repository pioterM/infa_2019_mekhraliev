V = 10 # Максимальная скорость шариков

from tkinter import *
from random import randrange as rnd, choice, random
import time
root = Tk()
root.geometry('800x600')
root.title('Шарики')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH,expand=1)

lbl_score = Label(canv)
lbl_score.pack()
score = 0

ball_1 = {
	'ball_id': 0
}

ball_2 = {
	'ball_id': 0
}

colors = ['red','orange','yellow','green','blue']
def new_ball(ball):
	direction = [-1, 1]
	ball['step_x'] = V * choice(direction) * random()
	ball['step_y'] = V * choice(direction) * random()
	if ball['ball_id']:
		canv.delete(ball['ball_id'])
	ball['is_new_ball'] = True
	ball['x'] = rnd(100,700)
	ball['y'] = rnd(100,500)
	ball['r'] = rnd(30,50)
	ball['color'] = choice(colors)
	ball['ball_id'] = canv.create_oval(round(ball['x']-ball['r']),round(ball['y']-ball['r']),round(ball['x']+ball['r']),round(ball['y']+ball['r']),fill = ball['color'], width=0)
	ball['redraw_id'] = root.after(10000, new_ball, ball)
	return ball

def move_ball(ball):
	if ball['x'] + ball['r'] >= 800 or ball['x'] - ball['r'] <= 0:
		ball['step_x'] *= -1
	if ball['y'] + ball['r'] >= 600 or ball['y'] - ball['r'] <= 0:
		ball['step_y'] *= -1
	ball['x'] += ball['step_x']
	ball['y'] += ball['step_y']
	canv.move(ball['ball_id'], ball['step_x'], ball['step_y'])
	root.after(10, move_ball, ball)
	return ball

def click(event, ball):
	global score
	if (ball['x'] - event.x)**2 + (ball['y'] - event.y)**2 <= ball['r']**2 and ball['is_new_ball']:
		score += 1
		ball['is_new_ball'] = False
		lbl_score['text'] = 'Счет: ' + str(score)
		root.after_cancel(ball['redraw_id'])
		new_ball(ball)

ball_1 = new_ball(ball_1)
ball_1 = move_ball(ball_1)
ball_2 = new_ball(ball_2)
ball_2 = move_ball(ball_2)
lbl_score['text'] = 'Счет: 0'
canv.bind('<Button-1>', lambda event: (click(event, ball_1), click(event, ball_2)))
mainloop()
