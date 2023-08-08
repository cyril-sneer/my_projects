import turtle
import random
import my_graphics

WIDTH = 600
HEIGHT = 600
BUILDINGS = 6
BUILDING_WIDTH = WIDTH/BUILDINGS
LINE = {}


def draw_city():
    turtle.penup()

    start_point_x = -WIDTH/2
    start_point_y = random.randint(-HEIGHT/4,HEIGHT/2)
    turtle.goto(start_point_x, start_point_y)
    turtle.pencolor('gray')
    turtle.fillcolor('gray')

    turtle.pendown()
    turtle.begin_fill()
    for b in range(BUILDINGS):
        next_point_x = turtle.xcor() + BUILDING_WIDTH                           # вычисляем коордитаты след точки по гор
        next_point_y = turtle.ycor()

        for x_cor in range(int(turtle.xcor()), int(turtle.xcor() + BUILDING_WIDTH + 1)):
            LINE[x_cor] = turtle.ycor()                                         # записать координаты в словарь

        turtle.goto(next_point_x, next_point_y)                                 # рисуем горизонтальную линию

        next_point_x = turtle.xcor()
        next_point_y = random.randint(-HEIGHT/4,HEIGHT/2)                       # вычисляем коордитаты след точки по верт
        turtle.goto(next_point_x, next_point_y)                                 # рисуем вертикальную линию

    # замкнуть контур снизу
    turtle.goto(WIDTH/2,-HEIGHT/2)
    turtle.goto(-WIDTH/2, -HEIGHT/2)
    turtle.goto(start_point_x, start_point_y)
    turtle.end_fill()
    turtle.penup()


def draw_stars(quantity:int):
    for i in range(quantity):
        x_cor = random.randint(-WIDTH/2, WIDTH/2)
        y_cor = random.randint(LINE[x_cor],HEIGHT/2)
        my_graphics.circle(x_cor, y_cor, 2, 'white')


def draw_windows(quantity:int):
    for i in range(quantity):
        x_cor = random.randint(-WIDTH/2, WIDTH/2)
        y_cor = random.randint(-HEIGHT/2, LINE[x_cor])
        my_graphics.square(x_cor, y_cor, 10, 'yellow')


def main():
    turtle.setup(WIDTH, HEIGHT)
    turtle.bgcolor('blue')
    turtle.speed(0)
    turtle.hideturtle()

    draw_city()
    draw_stars(random.randint(1,10))
    draw_windows(20)


main()
turtle.exitonclick()


