import turtle

#variables
pen_color = str()
fill_color = str()
pen_size = int()

#moving the pen
turtle.penup()
turtle.goto(0,150)
turtle.pendown()

#user input
pen_size = int(input('Choose pen size from 1 to 10 '))
pen_color = input('red, yellow, and blue ')

#color
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'yellow':
    fill_color = 'green'
else:
    fill_color = 'red'

turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

turtle.begin_fill()
#draw cirlcle
turtle.circle(50)
#stopping the fill
turtle.end_fill()

#move pen
turtle.penup()
turtle.goto(-90,0)
turtle.pendown()

#user input
pen_color = input('red, yellow, blue ')


#color
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'yellow':
    fill_color = 'green'
elif pen_color == 'blue':
    fill_color = 'red'

turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)
turtle.begin_fill()

#square
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.end_fill()

#move pen
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()


pen_color = input('red, yellow, blue ')


#color
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'yellow':
    fill_color = 'green'
elif pen_color == 'blue':
    fill_color = 'red'


turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)
turtle.begin_fill()

#triangle
turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)

turtle.end_fill()



#####################


#variables
shape = str()
location = str()
pen_color = str()
fill_color = str()

#user input
shape = input('Circle or square ')
location = input('Top left, top right, bottom left, bottom right ')

#colors
if shape == 'circle':
    pen_color = input('red, blue, or yellow for pen color ')
    turtle.pencolor(pen_color)
    if pen_color == 'red':
        fill_color = 'orange'
    elif pen_color == 'blue':
        fill_color = 'green'
    else:
        fill_color = 'black'
elif shape == 'square':
    fill_color = input('red blue, or yellow for fill color ')
    turtle.fillcolor(fill_color)
    if fill_color == 'red':
        pen_color = 'orange'
    elif fill_color == 'blue':
        pen_color = 'green'
    else:
        pen_color = 'black'

turtle.fillcolor(fill_color)
turtle.pencolor(pen_color)

#drawing shapes
if shape == 'circle':
    if location == 'top left':
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(-150,150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
    elif location == 'top right':
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(150,150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
    elif location == 'bottom left':
        turtle.pensize(7)
        turtle.penup()
        turtle.goto(-150,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
    elif location == 'bottom right':
        turtle.pensize(9)
        turtle.penup()
        turtle.goto(150,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
elif shape == 'square':
    if location == 'top left':
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(-300,150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()
    elif location == 'top right':
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(300,150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()
    elif location == 'bottom left':
        turtle.pensize(7)
        turtle.penup()
        turtle.goto(-300,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()
    elif location == 'bottom right':
        turtle.pensize(9)
        turtle.penup()
        turtle.goto(300,-150)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()




















        
