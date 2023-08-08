import turtle

class Coords:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def draw_triangle(apex_1:Coords, apex_2:Coords, apex_3:Coords, color:str):
    save_color = turtle.pencolor()
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(apex_1.x, apex_1.y)
    turtle.pendown()
    turtle.goto(apex_2.x, apex_2.y)
    turtle.goto(apex_3.x, apex_3.y)
    turtle.goto(apex_1.x, apex_1.y)
    turtle.penup()
    turtle.pencolor(save_color)


def main():
    turtle.hideturtle()
    point_1 = Coords(-100,-100)
    point_2 = Coords(100, -100)
    point_3 = Coords(0,100)
    draw_triangle(point_1, point_2, point_3, color='red')


main()
turtle.exitonclick()

