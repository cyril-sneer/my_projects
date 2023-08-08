# DISTANCE = SPEED * TIME

speed = float(input('Введите скорость:\t'))
t = int(float(input('Введите время движения:\t')))

print('Time\tDistance')
print('-' * 15)

for i in range(1, t+1):
    print(f'{i : d}\t\t{i * speed : .2f}')
