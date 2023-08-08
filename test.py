SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE


def my_func(*args) -> None:
    print(len(args))
    print(args)
    for i in args:
        print(i, end=" ")
    print()
    for i in range(len(args)):
        print(args[i], end=" ")
    print()


my_func(1, 2, 4, 7, "s", "d", True, [1, 2, 3])


def my_gen():
    my_list = [1, 2, 3, "a", 'b', "c"]
    for l in my_list: yield l


for j in my_gen():
    print(j)

