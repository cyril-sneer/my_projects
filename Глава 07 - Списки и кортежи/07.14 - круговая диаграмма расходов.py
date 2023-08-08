import matplotlib.pyplot as plt

DATA_FILE_NAME = r'data\expenses.txt'
EXPENSES_LABELS = ["Аренда", "Бензин", "Продукты питания", "Одежда", "Содержание авто", "Прочее"]

data_file = open(DATA_FILE_NAME, 'r')
expenses = [float(exp.rstrip()) for exp in data_file.readlines()]
data_file.close()

plt.pie(expenses, labels = EXPENSES_LABELS)
plt.title('Расходы за месяц')


plt.show()