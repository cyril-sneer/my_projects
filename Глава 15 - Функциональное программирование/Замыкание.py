def make_adder():
    n = 0
    def fn(x):
        nonlocal n
        n += x
        return n
    return fn

my_adder = make_adder()

print(my_adder(5))
print(my_adder(7))

print()

def adder(n):
    def fn(m):
        return n + m
    return fn

sum_three = adder(3)
print(sum_three)
print(sum_three(1))
print(sum_three(5))

print()

adder = lambda n: lambda m: n + m

sum_three = adder(3)
print(sum_three)
print(sum_three(1))
print(sum_three(5))

print()
def power_generator(base):
    return lambda x: pow(x, base)

square = power_generator(2)
print(square)
print(square(3))

cube = power_generator(3)
print(cube)
print(cube(3))


print()
def make_adder():
    n = 0
    def fn(x):
        nonlocal n
        n += x
        return n
    return fn

my_adder = make_adder()
print(my_adder(5))
print(my_adder(2))
print(my_adder(3))

