#!/usr/bin/env python

import turtle
import sys
import math

foo = sys.argv[1]
foo = int(foo)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('hello world')

wario = turtle.Turtle()
wario.color('blue')
wario.pensize(1)

def triangle():
    wario.forward(80)
    wario.left(120)
    wario.forward(80)
    wario.left(120)
    wario.forward(80)
    wario.left(120)

def square():
    wario.forward(100)
    wario.left(90)
    wario.forward(100)
    wario.left(90)
    wario.forward(100)
    wario.left(90)
    wario.forward(100)
    wario.left(90)

def triangle2():
    for i in range(3):
        wario.forward(80)
        wario.left(120)

def square2():
    for i in range(4):
        wario.forward(80)
        wario.left(90)

def shape(x):
    sides = 360/x
    height = math.log(sides) * 3
    for i in range(x):
        wario.forward(height)
        wario.left(sides)

if __name__ == '__main__':
    for i in range(3,14):
        shape(i)
        wario.forward(40)

    wn.mainloop()
