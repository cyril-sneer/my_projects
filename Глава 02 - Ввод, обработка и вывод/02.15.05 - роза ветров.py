import turtle

CENTER_X = 0
CENTER_Y = 0
AXIS_LENGTH = 300
RADIUS = AXIS_LENGTH / 10
EAST = 0
SOUTH = 270

turtle.speed(7)
turtle.hideturtle()

# horizontal axis
x = CENTER_X - AXIS_LENGTH / 2
y = CENTER_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(AXIS_LENGTH)

# vertical axis
x = CENTER_X
y = CENTER_Y + AXIS_LENGTH / 2
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.forward(AXIS_LENGTH)

# circle
turtle.penup()
turtle.goto(CENTER_X, CENTER_Y - RADIUS)
turtle.pendown()
turtle.setheading(EAST)
turtle.circle(RADIUS)

# text
turtle.penup()
turtle.goto(CENTER_X, CENTER_Y + AXIS_LENGTH / 2)
turtle.write('North', False, align='center', font=('Calibri', 12, 'normal'))
turtle.goto(CENTER_X, CENTER_Y - AXIS_LENGTH / 2 - 15)
turtle.write('South', False, align='center', font=('Calibri', 12, 'normal'))
turtle.goto(CENTER_X + AXIS_LENGTH / 2, CENTER_Y)
turtle.write('East', False, align='left', font=('Calibri', 12, 'normal'))
turtle.goto(CENTER_X - AXIS_LENGTH / 2, CENTER_Y)
turtle.write('West', False, align='right', font=('Calibri', 12, 'normal'))

turtle.done()

