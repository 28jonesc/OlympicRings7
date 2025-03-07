import turtle

screen = turtle.Screen()
screen.screensize(500,500)

t = turtle.Turtle()

screen.bgcolor("tan")
t.penup()
t.goto(-80,15)
t.pencolor("blue")
t.pendown()
t.circle(35)
t.penup()

t.goto(0,15)
t.pencolor("black")
t.pendown()
t.circle(35)
t.penup()

t.goto(80,15)
t.pencolor("red")
t.pendown()
t.circle(35)
t.penup()

t.goto(-40,-15)
t.pencolor("yellow")
t.pendown()
t.circle(35)
t.penup()

t.goto(40,-15)
t.pencolor("green")
t.pendown()
t.circle(35)
t.penup()

t.pencolor("purple")
t.goto(0,-65)
t.pendown()
t.write("2026",font=("Ariel",30,"bold italic"),align="center")
t.penup()
t.goto(0,90)
t.write("Winter Olympics",font=("Ariel",30,"bold italic"),align="center")

#No code after this line
turtle.done()