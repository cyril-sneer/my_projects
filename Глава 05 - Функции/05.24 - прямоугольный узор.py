import turtle


class Coords:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def read_size()->tuple[int, int]:
    width = int(turtle.numinput('Введите значение', 'Введите ширину узора'))
    height = int(turtle.numinput('Введите значение', 'Введите высоту узора'))
    return width, height


def calc_apexes(width:int, height:int)->tuple[Coords, Coords, Coords, Coords]:
    left_bottom = Coords(-int(width/2), -int(height/2))
    left_top = Coords(left_bottom.x, left_bottom.y + height)
    right_top = Coords(left_bottom.x + width, left_bottom.y + height)
    right_bottom = Coords(left_bottom.x + width, left_bottom.y)
    return left_bottom, left_top, right_top, right_bottom


def draw_rectangle(width:int, height:int):
    left_bottom, left_top, right_top, right_bottom = calc_apexes(width, height)
    turtle.penup()
    turtle.goto(left_bottom.x, left_bottom.y)
    turtle.pendown()
    turtle.goto(right_bottom.x, right_bottom.y)
    turtle.goto(right_top.x, right_top.y)
    turtle.goto(left_top.x, left_top.y)
    turtle.goto(left_bottom.x, left_bottom.y)
    turtle.penup()


def draw_line(start:Coords, end:Coords):
    turtle.penup()
    turtle.goto(start.x, start.y)
    turtle.pendown()
    turtle.goto(end.x, end.y)
    turtle.penup()


def main():
    turtle.hideturtle()
    turtle.speed(0)

    pattern_width, pattern_height = read_size()

    draw_rectangle(width=pattern_width, height=pattern_height)
    draw_rectangle(width=int(pattern_width * 0.75), height=int(pattern_height * 0.75))
    turtle.begin_fill()
    draw_rectangle(width=int(pattern_width * 0.5), height=int(pattern_height * 0.5))
    turtle.end_fill()

    left_bottom, left_top, right_top, right_bottom = calc_apexes(pattern_width, pattern_height)
    mid_top = Coords(0, int(pattern_height/2))
    mid_bottom = Coords(0, int(-pattern_height/2))
    mid_left = Coords(int(-pattern_width/2), 0)
    mid_right = Coords(int(pattern_width/2), 0)

    draw_line(left_bottom, right_top)
    draw_line(left_top, right_bottom)
    draw_line(mid_left, mid_right)
    draw_line(mid_top, mid_bottom)


main()
turtle.exitonclick()