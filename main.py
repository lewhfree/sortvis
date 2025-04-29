import tkinter as tk
from sorters import *

def drawArray(array:list, canvas):
    canvas.delete('all')
    width = 400
    height = 400
    barWidth = int(width / len(array))
    a = 0
    for i in array:
        xs = a * barWidth + 1
        ys = height - (i * 10)
        xe = (a+1) * barWidth - 1
        ye = height

        canvas.create_rectangle(xs, ys, xe, ye, fill="blue")
        a += 1
root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=True)
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

array = [3, 4, 5, 1, 2, 5, 7, 6, 8]

sorter = Bubble(array)

drawArray(array, canvas)
canvas.pack()
root.mainloop()
