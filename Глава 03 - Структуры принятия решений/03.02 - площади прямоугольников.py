first_length = float(input('Введите длину первого прямоугольника:\t'))
first_width = float(input('Введите ширину первого прямоугольника:\t'))

second_length = float(input('Введите длину ВТОРОГО прямоугольника:\t'))
second_width = float(input('Введите ширину ВТОРОГО прямоугольника:\t'))

first_square = first_length * first_width
second_square = second_length * second_width

if first_square > second_square:
    print('Площадь первого прямоугольника больше')
elif second_square > first_square:
    print('Площадь ВТОРОГО прямоугольника больше')
else:
    print('Площади прямоугольников равны')
