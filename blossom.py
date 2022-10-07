import turtle
t = turtle.Pen()
t.shape('turtle')
turtle.bgcolor('#f4cbc7')


def worm():
    for i in range(3):
        t.pen(pencolor='#9FD983', fillcolor='#64BB6A', pensize=8, speed = 10)
        t.begin_fill()
        t.circle(20)
        t.penup()
        t.left(45)
        t.forward(52)
        t.pendown()
        t.end_fill()
def wormtail():
    for i in range(2):
        t.pen(pencolor='#9FD983', fillcolor='#64BB6A', pensize=8, speed = 10)
        t.begin_fill()
        t.circle(20)
        t.penup()
        t.forward(40)
        t.pendown()
        t.end_fill()

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def flower():
    for i in range(6):
        t.pen(pencolor='#de6600', fillcolor='#fea02f', pensize=8, speed = 10)
        t.begin_fill()
        t.circle(40)
        t.penup()
        t.left(60)
        t.forward(110)
        t.pendown()
        t.end_fill()
    Go(-230,200)


def flowerpart2():
    t.color('#977655')
    t.pensize('6')
    n=5
    while n <= 40:
        t.circle(n)
        n += 5
        
        
def stem():
    for i in range(4):
        t.pen(pencolor='#977655', fillcolor='#51E17E', pensize=6, speed = 10)
        t.begin_fill()
        t.forward(100)
        t.left(20)
        t.end_fill()
worm()
t.penup()
t.home()
t.right(90)
t.forward(12)
t.pendown()
wormtail()
worm()
Go(-150,200)
flower()
flowerpart2()
t.penup()
Go(-255,145)
t.right(135)
stem()

