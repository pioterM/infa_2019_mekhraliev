from graph import *
#brushColor("yellow")
def ellipse(x0, y0, a, b):
    k = ()
    p = []
    y = 0
    for x in range(x0-a,x0+a,1):
        y = round(y0 + b*(1-((x-x0)**2/a**2))**0.5)
        k = (x, y)
        p.append(k)
    for x in range(x0+a, x0-a-1, -1):
        y = round(y0 - b*(1-((x-x0)**2/a**2))**0.5)
        k = (x, y)
        p.append(k)
    polygon(p)
windowSize(426, 604)

ellipse(200, 200, 125, 75)

run()