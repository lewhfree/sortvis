def drawArray(array:list, canvas, index, done:bool, maxnum):
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
