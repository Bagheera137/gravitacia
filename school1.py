import turtle
def straight(x):
    y=2-x
    return y+60

def gorizontal(x):
    y=0
    return y
def parabola(x):
    y=x**2
    return y/100
def parabola2(x):
    y=50-x**2
    return y/100+100

def grafic(def_grafic):
    turtle.penup()
    turtle.goto(-200,def_grafic(-200))

    for i in range(-200,200):
        turtle.pendown()
        turtle.goto(i+1,def_grafic(i+1))
        turtle.penup()


screen=turtle.Screen()
turtle.tracer(0)

grafic(gorizontal)
grafic(straight)
grafic(parabola)
grafic(parabola2)
for x in range(-300,300,10):
    for y in range(-400,400,10):
        turtle.goto(x,y)
        if y>parabola(x) and y>parabola2(x) and x>0:
            turtle.dot(4,"red")
        if y>straight(x) and y<parabola(x) and x<0:
            turtle.dot(4, "red")
        if y>parabola(x) and y<parabola2(x) and x<0 and y<straight(x):
            turtle.dot(4,"red")
        if y<parabola(x) and y<parabola2(x) and x>0 and y<straight(x) and y>0:
            turtle.dot(4,"red")
screen.update()
turtle.done()