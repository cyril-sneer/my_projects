import turtle

CENTER_X = 0
CENTER_Y = 0
LEFT_UP_X = -100
LEFT_UP_Y = 100
LEFT_DOWN_X = -100
LEFT_DOWN_Y = - 100
RIGHT_UP_X = 100
RIGHT_UP_Y = 100
RIGHT_DOWN_X = 100
RIGHT_DOWN_Y = - 100
side_length = RIGHT_UP_X - LEFT_UP_X

turtle.speed(7)
turtle.hideturtle()

turtle.goto(CENTER_X, CENTER_Y)
turtle.dot()
turtle.goto(LEFT_DOWN_X, LEFT_DOWN_Y)
turtle.dot()
turtle.goto(LEFT_UP_X, LEFT_UP_Y)
turtle.dot()
turtle.goto(RIGHT_DOWN_X, RIGHT_DOWN_Y)
turtle.dot()
turtle.goto(RIGHT_UP_X, RIGHT_UP_Y)
turtle.dot()
turtle.goto(CENTER_X, CENTER_Y)

turtle.penup()
turtle.goto(LEFT_UP_X, LEFT_UP_Y)
turtle.setheading(0)

for i in range(1, 10):
    if i % 2 != 0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(side_length / 9)

turtle.penup()
turtle.goto(LEFT_DOWN_X, LEFT_DOWN_Y)
turtle.setheading(0)

for i in range(1, 10):
    if i % 2 != 0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(side_length / 9)


turtle.done()
