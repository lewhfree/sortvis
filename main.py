import tkinter as tk
from sorters import *
import time
import random
from draw import *
maxnum = 90

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True)
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

array = list(range(1, maxnum))
random.shuffle(array)

sorter = Bubble(array)
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
