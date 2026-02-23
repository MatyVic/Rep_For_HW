# Перевірка на парність без використання /, //, % та divmod


def is_even(number):
    str_number = str(number)
    return int(str_number[-1]) in (0, 2, 4, 6, 8)


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(350**2) == True, 'Test4'
print('OK')
