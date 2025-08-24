# This program explains the range function into a list

import turtle

wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

jose.speed(0.6)

for size in range(10):
    jose.forward(50)
    jose.stamp()
    jose.forward(-50)
    jose.right(36)
wn.exitonclick()
    