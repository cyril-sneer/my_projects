# -*- coding: utf-8 -*-

# Игра "Порази цель"
import turtle
import math

# Именованные константы
SCREEN_WIDTH = 600     # Ширина экрана
SCREEN_HEIGHT = 600    # Высота экрана
TARGET_LLEFT_X = 100   # Левая нижняя координата X цели
TARGET_LLEFT_Y = 250   # Левая нижняя координата Y цели
TARGET_WIDTH = 25      # Ширина цели
FORCE_FACTOR = 30      # Фактор произвольной силы
PROJECTILE_SPEED = 1   # Скорость анимации снаряда
NORTH = 90             # Угол северного направления
SOUTH = 270            # Угол южного направления
EAST = 0               # Угол восточного направления
WEST = 180             # Угол западного направления

# Настроить окно.
while True:
   
    #turtle.reset()
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Нарисовать цель.
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()

    # Центрировать черепаху.
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)

    # Получить угол выстрела и силу от пользователя.
    angle = float(input("Введите угол выстрела снаряда: "))
    force = float(input("Введите пусковую силу (1−10): "))
    if angle == force == 0:
        turtle.bye()
        break

    # Рассчитать расстояние.
    distance = force * FORCE_FACTOR

    # Задать направление
    turtle.setheading(angle)

    # Запустить снаряд.
    turtle.pendown()
    turtle.forward(distance)

    # Снаряд поразил цель?
    if (TARGET_LLEFT_X <= turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)) and \
        (TARGET_LLEFT_Y <= turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Цель поражена!')
        turtle.exitonclick()
        break
    else:
        print('Вы промахнулись.')
        min_degree = math.degrees(math.atan(TARGET_LLEFT_Y / (TARGET_LLEFT_X+TARGET_WIDTH)))
        max_degree = math.degrees(math.atan((TARGET_LLEFT_Y + TARGET_WIDTH) / TARGET_LLEFT_X))
        if turtle.heading() < min_degree: print('Угол слишком мал, увеличьте!')
        elif turtle.heading() > max_degree: print('Угол слишком велик, нужно уменьшить!')
        else:
            print('С таким углом вам пожет повезти!')
            if turtle.xcor() < TARGET_LLEFT_X or turtle.ycor() < TARGET_LLEFT_Y:
                print('Слабо бьешь, товарищ! Нужно сильнее!')
            else:
                print('Не так сильно, тигр! Давай слабее!')


# turtle.done()
