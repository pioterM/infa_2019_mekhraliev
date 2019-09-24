from graph import *

N = 200
x1 = 100;
y1 = 100
x2 = x1 + 10 * N;
y2 = 200

rectangle(x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
    line(x, y1, x, y2)
    x += h

run()
