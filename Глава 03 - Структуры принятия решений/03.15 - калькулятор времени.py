MIN = 60
HOUR = 3600
DAY = 86400

while True:
    time_in_seconds = int(input('Введите колчество секунд:\t'))
    if time_in_seconds == 0: break

    days = time_in_seconds // DAY
    hours = time_in_seconds % DAY // HOUR
    minutes = time_in_seconds % DAY % HOUR // MIN
    seconds = time_in_seconds % MIN

    print(f'Days - {days:.0f} : Hours - {hours:.0f} : Minutes - {minutes:.0f} : Seconds - {seconds:.0f}')

    msg = 'Seconds - {seconds:.0f}'
    if time_in_seconds >= MIN: msg = 'Minutes - {minutes:.0f} : ' + msg
    if time_in_seconds >= HOUR: msg = 'Hours - {hours:.0f} : ' + msg
    if time_in_seconds >= DAY: msg = 'Days - {days:.0f} : ' + msg
    msg = "print(f'" + msg + "')"
    exec(msg)

    # if time_in_seconds >= DAY:
    #     print(f'Days - {days:.0f} : Hours - {hours:.0f} : Minutes - {minutes:.0f} : Seconds - {seconds:.0f}')
    # elif time_in_seconds >= HOUR:
    #     print(f'Hours - {hours:.0f} : Minutes - {minutes:.0f} : Seconds - {seconds:.0f}')
    # elif time_in_seconds >= MIN:
    #     print(f'Minutes - {minutes:.0f} : Seconds - {seconds:.0f}')
    # else:
    #     print(f'Seconds - {seconds:.0f}')
