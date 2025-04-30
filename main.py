import tkinter as tk
from sorters import *
import time
import random

maxnum = 90

def drawArray(array:list, canvas, index, done:bool):
    canvas.delete('all')
    width = 500
    height = 500
    barWidth = int(width / len(array))
    a = 0
    for i in array:
        xs = a * barWidth + 1
        ys = height - (i * (height / maxnum))
        xe = (a+1) * barWidth - 1
        ye = height
        firstGreater = int(array[index] == array[index - 1]) 

        if a==index:
            if firstGreater:
                fill = "red"
            else:
                fill = "green"
        elif a==index-1:
            if firstGreater:
                fill = "green"
            else:
                fill = "red"
        else:
            fill = "blue"

        if done:
            fill = "green"
        canvas.create_rectangle(xs, ys, xe, ye, fill=fill)
        a += 1

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

array = list(range(1, maxnum))
random.shuffle(array)

sorter = Bubble(array)
#sorter = Bogo(array)
drawArray(array, canvas, 1, False)
canvas.pack()
newArr = array
idx = 1
ddone = False

while True:
    #time.sleep(0.01)
    drawArray(newArr, canvas, idx, ddone)
    newArr, idx, ddone = sorter.step()
    canvas.pack()
    root.update()
