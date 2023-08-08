import turtle

LEFT_UP_X = -100
LEFT_UP_Y = 100
UP_X = 0
UP_Y = 100
RIGHT_X = 100
RIGHT_Y = 0
RIGHT_DOWN_X = 100
RIGHT_DOWN_Y = -100
DOWN_X = 0
DOWN_Y = -100
LEFT_X = -100
LEFT_Y = 0

turtle.speed(5)
turtle.hideturtle()

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.goto(LEFT_UP_X, LEFT_UP_Y)
turtle.pendown()
turtle.goto(RIGHT_DOWN_X, RIGHT_DOWN_Y)

turtle.penup()
turtle.goto(UP_X, UP_Y)
turtle.pendown()
turtle.goto(RIGHT_X, RIGHT_Y)

turtle.penup()
turtle.goto(LEFT_X, LEFT_Y)
turtle.pendown()
turtle.goto(DOWN_X, DOWN_Y)

turtle.done()
