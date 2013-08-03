import turtle
import time

turt = turtle.Turtle()
screen = turt.getscreen()
screen.bgcolor("lightgreen")

turt.color("purple")
turt.pensize(4)
turt.speed(2)

turt.penup()
turt.goto(-100,100)
turt.right(90)
for col in range(0,5):
    turt.pendown()
    turt.forward(200)
    turt.penup()
    turt.left(90)
    turt.forward(20)
    turt.left(90)
    turt.pendown()
    turt.forward(200)
    turt.penup()
    turt.right(90)
    turt.forward(20)
    turt.right(90)
turt.getscreen()._root.mainloop()
