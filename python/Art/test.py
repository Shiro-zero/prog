import random

def color_print(text,color):
    print("\033["+str(color)+"m" +text + "\033[0m")

def random_color_print(text):
    color_print(text,random.randint(30,36))

import turtle
from turtle import *

turtle.title("rainbow spiral")
speed(15)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(50+i)
    rt(91)
    pencolor(r,g,b)

done()


if False:
    for i in range(100):
        random_color_print("Hello, World!")
        #color_print("hello world"+str(i),i)