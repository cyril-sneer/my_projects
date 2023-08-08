ONE_ACR_IN_METERS = 4046.86

square_in_meters = float(input('Введите площадь участка в кв м: '))
square_in_acres = square_in_meters/ONE_ACR_IN_METERS

print(f'Площадь участка в акрах равна {square_in_acres:.2f}')
