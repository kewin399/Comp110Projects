"""
Module: name_drawer

A program to draw a name using one (or more) turtles.

Authors:
1) Cavin Nguyen - cavinnguyen@sandiego.edu 9/13/2024
"""
import turtle
import random


user_choice = input("Enter the color to use for the pen. (Type 'random' for random colors): ")


def randomize_color():
    color_options = ["red", "green", "orange", "yellow", "blue", "black", "brown", "pink", "cyan", "magenta", "turquoise"]
    rand_num = random.randint(0,7)
    color = color_options[rand_num]
    return color

wn = turtle.Screen()
if user_choice == "random":

    color0 = randomize_color()
    color1 = randomize_color()
    color2 = randomize_color()
    color3 = randomize_color()
    color4 = randomize_color()

else:
    color0 = user_choice
    color1 = user_choice
    color2 = user_choice
    color3 = user_choice
    color4 = user_choice


# Initialize turtles
# create turtle for letter "C", set its pen color and shape
letter0 = turtle.Turtle()
letter0.pencolor(color0)
letter0.shape("turtle")

# create turtle for letter "A" and set the pen color
letter1 = turtle.Turtle()
letter1.pencolor(color1)
letter1.shape("turtle")

# create turtle for letter "V" and set the pen color
letter2 = turtle.Turtle()
letter2.pencolor(color2)
letter2.shape("turtle")

# create turtle for letter "I" and set the pen color
letter3 = turtle.Turtle()
letter3.pencolor(color3)
letter3.shape("turtle")

# create turtle for letter "N" and set the pen color
letter4 = turtle.Turtle()
letter4.pencolor(color4)
letter4.shape("turtle")

# create turtle to draw a zig zag under the name, and set the pen color
underline = turtle.Turtle()
underline.pencolor("cyan")
underline.shape("turtle")

# This section declares the pen size for all instances of the 
letter0.pensize(20)
letter1.pensize(20)
letter2.pensize(20)
letter3.pensize(20)
letter4.pensize(20)
underline.pensize(20)

# This section of code lifts the pen, so that ink is not drawn onto the canvas, before an initial movement.
letter0.penup()
letter1.penup()
letter2.penup()
letter3.penup()
letter4.penup()
underline.penup()

# Set object initial position on wn for all turtle instances.
offset = 20
letter0.goto(-300 + offset, -50)
letter1.goto(-225 + offset, -50)
letter2.goto(-75 + offset, -50)
letter3.goto(40 + offset, -50)
letter4.goto(100 + offset, -50)
underline.goto(-400, -100)

# This section of code lowers the pen, so that ink can go onto the canva for all instances of turtles.
letter0.pendown()
letter1.pendown()
letter2.pendown()
letter3.pendown()
letter4.pendown()
underline.pendown()

# Turtle letter0 draws the letter C.
letter0.forward(20)
letter0.left(180)
letter0.forward(20)
for i in range(18):
    letter0.forward(10)
    letter0.right(10)
letter0.forward(30)
letter0.penup()
letter0.goto(250, -40)

# Turtle letter1 draws the letter A.
letter1.left(75)
letter1.forward(120)
letter1.right(75)
letter1.forward(30)
letter1.right(75)
letter1.forward(120)
letter1.right(180)
letter1.forward(120*(2/3))
letter1.left(75)
letter1.forward(45)
letter1.penup()
letter1.goto(250, -40)

# Turtle letter2 draws the letter V.
letter2.left(105)
letter2.forward(120)
letter2.left(180)
letter2.forward(120)
letter2.left(75)
letter2.forward(30)
letter2.left(75)
letter2.forward(120)
letter2.penup()
letter2.goto(250, -40)

# Turtle letter3 draws the letter I.
letter3.left(90)
letter3.forward(115)
letter3.penup()
letter3.goto(250, -40)

# Turtle letter4 draws the letter N.
letter4.left(90)
letter4.forward(120)
letter4.right(145)
letter4.forward(145)
letter4.left(145)
letter4.forward(120)
letter4.penup()
letter4.goto(250, -40)

# Changes underline object's drawing speed using .speed module
underline.speed(10)

# Draws underline turtle draws zig zag.
for i in range(25):
    underline.left(45)
    underline.forward(20)
    underline.right(90)
    underline.forward(20)
    underline.left(45)


# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()

