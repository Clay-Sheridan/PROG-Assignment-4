'''This is a square and a triangle'''
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")

alex = turtle.Turtle()
alex.pensize(5)

tom = turtle.Turtle()
tom.color("red")

alex.forward(80)
alex.left(120)
alex.forward(80)
alex.left(120)
alex.forward(80)
alex.left(120)

alex.right(180)
alex.forward(80)

tom.forward(50)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.left(90)

wn.exitonclick()