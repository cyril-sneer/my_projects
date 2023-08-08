from classes import employees


def main():
    boss = employees.ShiftSupervisor()
    
    id_num = int(input('Введите ID номер сотрудника: '))
    boss.set_id_num(id_num)
    
    name = input("Введите имя сотрудника: ")
    boss.set_name(name)
    
    year_salary = float(input("Введите годовую зарплату: "))
    boss.set_year_salary(year_salary)
    
    year_bonus = float(input("Введите годовой бонус: "))
    boss.set_year_bonus(year_bonus)
    
    print()
    print(boss)


if __name__ == '__main__':
    main()
