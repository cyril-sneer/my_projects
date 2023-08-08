books = int(input('Введите кол-во приобретенных книг:\t'))

score = 0

if books == 2: score = 5
elif books <= 4: score = 15
elif books <= 6: score = 30
elif books >= 7: score = 60
else: score = 0

print(f'Вы заработали {score:.0f} очков')