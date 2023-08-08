EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
QUANTITY = 30
STEP = 10

import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(200, -200)
turtle.pendown()

for d in range(1, QUANTITY+1):
    turtle.setheading(NORTH)
    turtle.forward(d * STEP)
    turtle.setheading(WEST)
    turtle.forward(d * STEP)
    turtle.setheading(SOUTH)
    turtle.forward(d * STEP)
    turtle.setheading(EAST)
    turtle.forward(d * STEP)

turtle.done()