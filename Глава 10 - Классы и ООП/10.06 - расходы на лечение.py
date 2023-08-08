from objects import med

patient_1 = med.Patient()
patient_1.set_name(fst_name='Sergey', scnd_name='Shapiro', fath_name='Olegovich')
patient_1.set_address(addr='Gagarin ave', city='Kharkiv', reg='Kharkiv', ind=61001)
patient_1.set_phone(ph='050 328-55-66')
patient_1.set_extra(name='Katia Shapiro', phone='095 350-50-50')

patient_1.add_proc(med.Procedure(title="Врачебный осмотр", date="06.03.2023", doctor="Ирвин", cost=250.00))
patient_1.add_proc(med.Procedure(title="Рентгенография", date="06.03.2023", doctor="Джемисон", cost=500.00))
patient_1.add_proc(med.Procedure(title="Анализ крови", date="06.03.2023", doctor="Смит", cost=200.00))

print("Данные о пациенте: ")
print(patient_1)
print("\nНазначенные процедуры: ")
for proc in patient_1.get_procs():
    print(proc)
print(f"\nОбщая стоимость лечения: {patient_1.get_treatment_cost():.2f}")
