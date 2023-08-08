import turtle


# class Coords:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y


def read_params():
    width = int(turtle.numinput('Введите значение', 'Введите ширину квадрата'))
    quantity = int(turtle.numinput('Введите значение', 'Введите количество квадратов'))
    return width, quantity


def square(x, y, width, color):
    turtle.penup()          # Поднять перо.
    turtle.goto(x, y)       # Переместить в указанное место.
    turtle.fillcolor(color) # Задать цвет заливки.
    turtle.pendown()        # Опустить перо.
    turtle.begin_fill()     # Начать заливку.
    for count in range(4):  # Нарисовать квадрат.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()


def main():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()

    width, quantity = read_params()

    y = -int(width*quantity/2)  # задать начальную позицию по вертикали

    for column in range(quantity):
        x = -int(width * quantity / 2)      # задать начальную позицию по горизонтали
        for row in range(quantity):
            if (row + column) % 2 == 0: color = 'black'
            else: color = ''
            square(x, y, width, color)
            x += width                      # сместить позицию по горизонтали на 1 квадрат
        y += width                          # сместить позицию по вертикали на 1 квадрат


main()
turtle.exitonclick()
