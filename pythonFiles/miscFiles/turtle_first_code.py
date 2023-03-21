#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

import turtle as t
from time import sleep

t.speed(0)
t.hideturtle()
a = 0

t.penup()
t.goto(0, -35)
t.pendown()

t.circle(57)

sleep(1)

t.penup()
t.goto(-170, -65)
t.pendown()

t.write('In an ideal world, this would be my text editing machine,\n\n\n\n\n\n\n\n\n'
        'and then my Mac would be my code-running machine!', font=("Calibre", 14, "normal"))

t.done()
