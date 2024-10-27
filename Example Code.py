# Use this file to show an "experienced" example of what you can create
# This code will run over and over!
from time import sleep
from turtle import *


def shuffle_color(index):  # Code used to shuffle colors
    if index == 0:
        color('red')
    if index == 1:
        color('orange')
    if index == 2:
        color('yellow')
    if index == 3:
        color('green')
    if index == 4:
        color('blue')
    if index == 5:
        color('indigo')
    if index == 6:
        color('violet')


# Driver code

def main():
    pendown()
    index = 0
    width(3)
    speed(20)
    for i in range(60):
        shuffle_color(index)
        index += 1
        if index == 7:
            index = 0
        circle(100)
        right(6)
    penup()
    left(90)
    forward(250)
    left(90)
    forward(550)
    # args = "Consider joining the Computer Science Honor Society!!!"
    args = "Example code"
    for i in range(len(args)):
        write(args[i], True, 'left', ("Arial", 40, "normal"))
        shuffle_color(index)
        index += 1
        if index == 7:
            index = 0
    forward(1200)
    left(90)
    forward(550)
    # args2 = "!!You must be taking/have taken a Computer Science Class to join!!"
    # color('red')
    # for i in range(len(args2)):
    #     write(args2[i], True, 'left', ("Arial", 30, "normal"))


if __name__ == "__main__":
    while True:
        main()
        sleep(3)
        clearscreen()
