import tkinter as tk
from sorters import *
from time import sleep
from random import shuffle
from draw import *

available = ""
for each in list(choices.keys()):
    available += each + "    "

print("Available algorithms: ", available)
choice = input("which sorting algorithm do you want to see? ").strip().lower()
sorter = choices.get(choice)
if not sorter:
    print("invalid choice")
    exit()

maxnum = int(input("How many numbers to sort? "))

array = list(range(1, maxnum + 1))
shuffle(array)

sorter = sorter(array)

print(sorter)

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True)
canvas = tk.Canvas(root, width=500, height=500)
drawArray(array, canvas, 1, False, maxnum)
canvas.pack()

newArr = array
idx = 1
ddone = False

while True:
    drawArray(newArr, canvas, idx, ddone, maxnum)
    newArr, idx, ddone = sorter.step()
    canvas.pack()
    root.update()
    if ddone:
        drawArray(newArr, canvas, idx, ddone, maxnum)
        canvas.pack()
        root.update()
        sleep(1)
        exit()
