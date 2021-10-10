import turtle 
from time import *
pen = turtle.Turtle()

def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 

def heart(): 
    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112) 
    pen.end_fill() 

def txt():
    sleep(1)
    pen.up() 
    pen.setpos(-35, 110) 
    pen.down() 
    pen.color('yellow')
    pen.write("Happy", font=("times", 18, "bold"))
    pen.up() 
    pen.setpos(-85, 80)
    pen.down()
    pen.color('yellow')
    pen.write("Valentine's Day !", font=("times", 18, "bold"))


heart() 
txt() 

pen.ht() 
sleep(5)
