from classes import employees


def main():
    worker = employees.ProductionWorker()
    
    id_num = int(input('Введите ID номер сотрудника: '))
    worker.set_id_num(id_num)
    
    name = input("Введите имя сотрудника: ")
    worker.set_name(name)
    
    shift = input("Введите номер смены (1/2): ")
    worker.set_shift(shift)
    
    hourly_rate = float(input("Введите почасовую ставку оплаты труда: "))
    worker.set_hourly_rate(hourly_rate)
    
    print(worker)


if __name__ == '__main__':
    main()
