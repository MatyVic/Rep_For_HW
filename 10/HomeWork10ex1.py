# ДЗ 10.1. Генераторна функція
from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    val = begin
    for _ in range(end):
        yield val
        val = func(val)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
