INPUT_FILE = r'data\steps.txt'

YEAR = {
    'JAN' : 31,
    'FEB' : 28,
    'MAR' : 31,
    'APR' : 30,
    'MAY' : 31,
    'JUN' : 30,
    'JUL' : 31,
    'AUG' : 31,
    'SEP' : 30,
    'OCT' : 31,
    'NOV' : 30,
    'DEC' : 31
}

step_file = open(INPUT_FILE, 'r')

for month in YEAR.keys():
    counter = 0
    for day in range(YEAR[month]):
        counter += int(step_file.readline())
    print(f'In {month} you walked {counter} steps. Average {counter/YEAR[month]:.0f} ')

step_file.close()
