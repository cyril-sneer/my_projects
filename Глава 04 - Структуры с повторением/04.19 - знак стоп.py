import turtle
import math

SIDE = 200

turtle.hideturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-SIDE * 0.5, SIDE * 0.5 + SIDE / math.sqrt(2))
turtle.pendown()
turtle.pensize(7)

turtle.fillcolor('red')
turtle.begin_fill()

for i in range(8):
    turtle.forward(SIDE)
    turtle.right(45)

turtle.end_fill()

turtle.penup()
turtle.goto(0, -45)
turtle.pendown()
turtle.write('STOP', move=False, align='center', font=('Colibry', 80, 'bold'))

turtle.exitonclick()
