from turtle import *

def spinner():

    forward(150)

    dot(120,"red")
    back(200)
    right(120)
    forward(200)

    dot(120,"blue")
    back(200)
    right(120)
    forward(200)

    dot(120,"green")
    back(200)
    right(120)
    update()
    
setup(500,500,None,None)
tracer(False)
width(20)
speed(1)
spinner()
done()
