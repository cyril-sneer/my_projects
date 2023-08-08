import turtle

INNER_TOP_X = 0
INNER_TOP_Y = 100
OUTER_TOP_X = 0
OUTER_TOP_Y = INNER_TOP_Y * 2
BASE_LEFT_X = -100
BASE_LEFT_Y = 0
BASE_RIGHT_X = 100
BASE_RIGHT_Y = 0

turtle.speed(5)
turtle.hideturtle()
turtle.penup()

turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)

turtle.pendown()
turtle.goto(OUTER_TOP_X, OUTER_TOP_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.goto(INNER_TOP_X, INNER_TOP_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.end_fill()

turtle.done()

