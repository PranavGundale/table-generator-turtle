""" Generates table using Python turtle.

@author: Pranav Gundale
Date: 31-12-2023
"""

import turtle
import lines
import draw

turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
turtle.speed(10)

num = input("Enter a number: ")

for i in range(int(num), int(num) * 10 + 1, int(num)):
    num_list = list(str(i))
    position = 1
    for num in num_list:
        print(position)
        position += 1
        draw.draw(lines.lines[int(num) - 1], 20)
        if position <= len(num_list):
            draw.next_character(20)
    print(num_list)
    for i in range(len(num_list) - 1):
        draw.go_left(20)
    draw.go_down(20)
