# Упражнение по программированию 2.11

# Процент учащихся обоего пола

# Переменные для количества учащихся женского и мужского пола,
# общего количества учащихся и процента учащихся
# женского и мужского пола.
male = 0
female = 0
total = 0
percentMale = 0.0
percentFemale = 0.0

# Получить количество учащихся мужского пола.
male = int(input("Введите количество учащихся мужского пола: "))

# Получить количество учащихся женского пола.
female = int(input("Введите количество учащихся женского пола: "))

# Вычислить общее количество учащихся.
total = male + female

# Вычислить процент учащихся мужского пола.
percentMale = male / total

# Вычислить процент учащихся женского пола.
percentFemale = female / total

# Напечатать процент учащихся мужского пола.
print("Юноши:", format(percentMale, '.2f'), "%")

# Напечатать процент учащихся женского пола.
print("Девушки:", format(percentFemale, '.2f'), "%")