# Декоратор – это обертка вокруг функции,
# которая определенным образом изменяет ее поведение.
# Существуют варианты использования декораторов,
# и вы, возможно, уже применяли их раньше
# при работе с такими фреймворками, как Flask.

def print_argument(func):
    def wrapper(the_number):
        print("Argument for",
              func.__name__,
              "is", the_number)
        return func(the_number)
    return wrapper

@print_argument
def add_one(x):
    return x + 1

add_one(1)

# Внутри print_argument мы определяем функцию-обертку.
# Она выводит аргумент и имя вызываемой функции,
# выполняет фактическую функцию и возвращает ее результат,
# как если бы функция вызывалась «обычно».
#
# С помощью @print_argument мы применяем наш декоратор к функции.
# Декоратор может быть повторно использован и для других функций.