import tkinter as tk
from sorters import *
import time
import random


def drawArray(array:list, canvas):
    canvas.delete('all')
    width = 500
    height = 500
    barWidth = int(width / len(array))
    a = 0
    for i in array:
        xs = a * barWidth + 1
        ys = height - (i * 20)
        xe = (a+1) * barWidth - 1
        ye = height

        canvas.create_rectangle(xs, ys, xe, ye, fill="blue")
        a += 1

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

array = list(range(10))
random.shuffle(array)

array = [1, 3, 5, 6, 2, 7, 9, 2]

sorter = Bubble(array)

drawArray(array, canvas)
canvas.pack()

while True:
    newArr = sorter.step()
    drawArray(newArr, canvas)
    canvas.pack()
    root.update()
    time.sleep(0.5)
