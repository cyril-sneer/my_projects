QUANTITY = 100
STEP = 5

import turtle

turtle.speed(0)

for i in range(QUANTITY):
    turtle.forward(STEP * i)
    turtle.left(90)

turtle.done()
