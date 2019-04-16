# 2.5 tkinter graphics cube

from tkinter import *
import math


def init(data):
    data.cx = data.width/2
    data.cy = data.height/2
    data.theta = math.pi*(2/3)
    data.axes = 3
    data.start = math.pi/2
    data.length = data.height/2
    data.side = 50

def keyPressed(event, data):
    pass

def mousePressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    for i in range(data.axes):
        # x1 = data.cx + data.length * math.cos(i*data.theta + data.start)
        # y1 = data.cy - data.length * math.sin(i*data.theta + data.start)
        # canvas.create_line(data.cx, data.cy, x1, y1, fill = "green")

        bottomx1 = data.cx + data.length/2 * math.cos(i*data.theta + data.start)
        bottomy1 = data.cy - data.length/2 * math.sin(i*data.theta + data.start)
        # canvas.create_line(data.cx, data.cy, bottomx1, bottomy1, fill = "black", \
        #     width = 10)

        canvas.create_line(data.cx, data.cy, data.cx, data.cy*(3/2), fill = "blue")

        if i != 0:
            topx1 = data.cx + data.length/2 * math.cos(i*data.theta + \
                data.start)
            topy1 = data.cy/2 - data.length/2 * math.sin(i*data.theta + \
                data.start)
            canvas.create_line(data.cx, data.cy/2, topx1, topy1, fill = "blue")

            canvas.create_line(topx1, topy1, bottomx1, bottomy1, fill = "blue")

            dx = topx1 - data.cx
            dy = topy1 - data.cy
            side = (dx**2 + dy**2) ** 0.5

            canvas.create_line(data.cx, data.cy*(3/2), bottomx1,bottomy1, fill = "blue")
            canvas.create_line(data.cx, data.cy, topx1, topy1, fill = "blue")
            

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed


run(800, 800)