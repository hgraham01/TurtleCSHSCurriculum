import tkinter as tk
from time import sleep
from turtle import *
def shuffle_color(index):
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
def square(size):
    for i in range(4):
        forward(size)
        right(90)
# def prompt():
#     user_key = input("What would you like to do? (r: retry, q: quit): ")
#     if user_key.lower() == "r":
#         clearscreen()
#         main()
#     elif user_key.lower() == "q":
#         print("Exiting program...")
#         exit()
#     else:
#         print("Try again with either a q(for quit) or r(for retry)!")
#         prompt()
#Driver code

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
    args = "Consider joining Computer Science Honor Society!!!"
    for i in range(len(args)):
        write(args[i], True, 'left', ("Arial", 40, "normal"))
        shuffle_color(index)
        index += 1
        if index == 7:
            index = 0
    forward(1200)
    left(90)
    forward(550)
    args2 = "!!You must be taking/have taken a Computer Science Class to join!!"
    color('red')
    for i in range(len(args2)):
        write(args2[i], True, 'left', ("Arial", 30, "normal"))
    # prompt()

if __name__ == "__main__":
    while True:
        main()
        sleep(3)
        clearscreen()
