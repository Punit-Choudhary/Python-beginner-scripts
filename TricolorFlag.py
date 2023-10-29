#Tricolor Flag

#Turtle Library
import turtle
turtle.bgcolor('grey')
tur=turtle.Turtle()
turtle.title('Happy Independence Day')
tur.penup()
tur.setpos(-200,200)
tur.speed(2)
c=['orange','green','white']
tur.width(4)

#orange
tur.fillcolor('orange')
tur.left(90)
tur.color(c[0])
tur.pendown()
tur.begin_fill()
for i in range(3):
    if i%2==0:
        tur.forward(80)
        tur.right(90)
    else:
        tur.forward(400)
        tur.right(90)
tur.end_fill()

#white
tur.fillcolor('white')
tur.color(c[2])
tur.begin_fill()
for j in range(4):
    if j%2==0:
        tur.forward(400)
        tur.left(90)
    else:
        tur.forward(80)
        tur.left(90)
tur.end_fill()

#Changing position of pen
tur.speed(100)
tur.penup()
tur.left(90)
tur.forward(80)
tur.pendown()
tur.speed(2)

#green
tur.color(c[1])
tur.fillcolor('green')
tur.begin_fill()
tur.forward(80)
tur.right(90)
tur.forward(400)
tur.right(90)
tur.forward(80)
tur.end_fill()

#Ashoka Chakra
tur.speed(10)
tur.penup()
tur.right(90)
tur.forward(230)
tur.left(90)
tur.forward(40)

tur.pendown()
tur.width(2)
tur.color('navyblue')
tur.circle(30)
tur.left(90)
tur.forward(60)
tur.left(90)

#strokes
for i in range(11):
    tur.circle(30,15,8)
    tur.left(90)
    tur.forward(60)
    tur.left(90)

#rod
tur.color('brown')
tur.width(10)
tur.left(90)
tur.penup()
tur.goto(-200,200)
tur.left(105)
tur.forward(80)
tur.left(180)
tur.pendown()
tur.forward(1500)


tur.hideturtle()
turtle.done()
    
