
def f1(*args, **kwargs):
    s = 0
    for i in args:
        if isinstance(i, (int, float)):
            s = s + i
    return s


print(f1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(f1())
print(f1(2, 4, 'abc', param_1=2))


def f2(x):
    if x == 0:
        return 0
    return x + f2(x-1)


def f3(x):
    if x <= 0:
        return 0
    if x % 2 == 0:
        return x + f3(x - 2)
    return f3(x-1)


def f4(x):
    if x <= 0:
        return 0
    if x % 2 == 1:
        return x + f4(x - 2)
    return f4(x-1)


def f5():
    nr = input()
    try:
        nr_int = int(nr)
        return nr
    except ValueError:
        return 0


print(f2(4))
print(f3(4))
print(f4(4))
print(f5())
