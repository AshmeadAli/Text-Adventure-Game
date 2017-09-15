from turtle import Turtle
from random import randint
a=Turtle()
b=Turtle()
c=Turtle()
a.color('red')
a.shape('turtle')
a.turtlesize(5,5,0) # a really big turtle !
b.color('blue')
b.shape('turtle')
c.color('black')
c.shape('turtle')
a.penup()
b.penup()
c.penup()
a.goto(-160,70)
b.goto(-160,40)
c.goto(-160,10)
for movement in range(100):
    a.forward(randint(1,5))
    b.forward(randint(1,5))           
    c.forward(randint(1,5))
