"""Contains functions to draw numbers and move the turtle."""

import turtle

def draw(a_list, length):
    if a_list[0] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    turtle.right(90)
    if a_list[1] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    if a_list[2] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    turtle.right(90)
    if a_list[3] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    turtle.right(90)
    if a_list[4] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    if a_list[5] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)
    turtle.penup()
    turtle.right(180)
    turtle.forward(length)
    turtle.left(90)
    turtle.pendown()
    if a_list[6] == True:
        turtle.pendown()
        turtle.forward(length)
    else:
        turtle.penup()
        turtle.forward(length)

def next_character(length):
    turtle.penup()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.pendown()

def go_left(length):
    turtle.penup()
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.pendown()

def go_down(length):
    turtle.penup()
    turtle.left(180)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.forward(length)
    turtle.left(90)
    turtle.pendown()
