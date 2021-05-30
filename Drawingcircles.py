import turtle
import time
import random

#variables
#horizontal = int()
#radius = int()
#colors = ['red', 'blue', 'yellow', 'green']
#pen_size = int()

#intitalizing the location and size of the circles
#horizontal = -200
#radius = 25
#pen_size = 2

#move pen
#turtle.penup()
#turtle.goto(horizontal, 0)
#turtle.pendown()

#initialize pensize
#turtle.pensize(5)

#loop to draw the circles
#for count in range(0, 4):
    #set the fill color, pen size, and fill color
    #turtle.pensize(pen_size)
    #turtle.begin_fill()
    #draw circle
    #turtle.circle(radius)
    #reset loction, radius, and pen size
    #horizontal = horizontal + 75
    #radius = radius + 20
    #pen_size = pen_size + 2
    #moving the turtle
    #turtle.penup()
    #turtle.goto(horizontal, 0)
    #turtle.pendown()
    #turtle.end_fill()

#new screen
time.sleep(3)
turtle.reset()
turtle.setup(600, 600)

#variables
radius = int()
colors = ['red', 'blue', 'yellow', 'green']
pen_size = int()
x = int()
y = int()
counter = int()
color = int()

#initialize variables
x = random.randint(-150, 150)
y = random.randint(-150, 150)
radius = random.randint(25, 125)
color = random.randint(0, 3)
pen_size = random.randint(0, 10)
counter = 1

#writing
turtle.write('Ready for more circles?', False, align = 'center', font = ('Ariel', 16, 'bold'))
time.sleep(3)
turtle.clear()
#loop
while counter <= 20:
    #set fill color, pen size, and fill color
    turtle.fillcolor(colors[color])
    turtle.pensize(pen_size)
    turtle.begin_fill()
    #move turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    #draw circle
    turtle.circle(radius)
    #end fill
    turtle.end_fill()
    #incriment
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    radius = random.randint(25, 125)
    color = random.randint(0, 3)
    pen_size = random.randint(0, 10)
    counter = counter + 1


























