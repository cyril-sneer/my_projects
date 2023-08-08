import turtle

turtle.speed(10)
turtle.hideturtle()
turtle.penup()
turtle.pensize(5)

R = turtle.numinput('Введите данные', 'Введите радиус окружностей')

RATE = 2.5          # соотношение межцентровых расстояний по горизонтали и радиуса окружностей

# центр первой окружности
C1_X = - R * RATE
C1_Y = 0
C1_COLOR = 'blue'

# центр второй окружности
C2_X = 0
C2_Y = 0
C2_COLOR = 'black'

# центр третьей окружности
C3_X = R * RATE
C3_Y = 0
C3_COLOR = 'red'

# центр четвертой окружности
C4_X = - (R * RATE) / 2
C4_Y = - (R * RATE) / 2
C4_COLOR = 'yellow'

# центр пятой окружности
C5_X = (R * RATE) / 2
C5_Y = - (R * RATE) / 2
C5_COLOR = 'green'

#turtle.setheading(-90)

turtle.goto(C1_X - R, C1_Y)
turtle.pendown()
turtle.pencolor(C1_COLOR)
turtle.circle(R)
turtle.penup()

turtle.goto(C2_X - R, C2_Y)
turtle.pendown()
turtle.pencolor(C2_COLOR)
turtle.circle(R)
turtle.penup()

turtle.goto(C3_X - R, C3_Y)
turtle.pendown()
turtle.pencolor(C3_COLOR)
turtle.circle(R)
turtle.penup()

turtle.goto(C4_X - R, C4_Y)
turtle.pendown()
turtle.pencolor(C4_COLOR)
turtle.circle(R)
turtle.penup()

turtle.goto(C5_X - R, C5_Y)
turtle.pendown()
turtle.pencolor(C5_COLOR)
turtle.circle(R)
turtle.penup()

turtle.done()
