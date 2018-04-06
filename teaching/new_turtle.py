#!/usr/bin/env python

import turtle

# Window
wn = turtle.Screen()
wn.bgcolor('green')
wn.title('Tutorial')


# The turtle
wario = turtle.Turtle()
wario.color('blue')
wario.pensize(2)


# Drawing stuff
def triangle():
    wario.forward(80)
    wario.left(120)
    wario.forward(80)
    wario.left(120)
    wario.forward(80)
    wario.left(120)


def triangle2():
    for i in range(3):
        wario.forward(80)
        wario.left(120)


def square():
    wario.forward(80)
    wario.left(90)
    wario.forward(80)
    wario.left(90)
    wario.forward(80)
    wario.left(90)
    wario.forward(80)
    wario.left(90)

def square2():
    for i in range(4):
        wario.forward(80)
        wario.left(90)

# Fernando's shape
def shape(number_of_sides):
    turn = 360 / number_of_sides
    for i in range(number_of_sides):
        wario.forward(80)
        wario.left(turn)

# Run this code
for i in range(1, 12):
    shape(i)

# Ask the user to close the window
wn.mainloop()
