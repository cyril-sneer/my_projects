names = ['Serge', 'Alex', 'Rubi', 'Roman']

_name = input('Enter name for search:  ')

if _name in names:
    print(f'Hi, {_name}!')
else:
    print(f'{_name} not found!')

list2 = [item for item in list1 if item % 2 == 0]