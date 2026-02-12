# ДЗ 8.3. Унікальне число
# Якщо унікальних значень не має программа має повернути None

def find_unique_value(some_list):
    unq_num = None
    for uniq in some_list:
        count = 0
        for val in some_list:
            if uniq == val:
                count += 1
        if count == 1:
            unq_num = uniq
            break

    return unq_num


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([5, 5, 5, 2, 2, 2]) == None, 'Test4'
assert find_unique_value([5, 5, 5, 0, 1, 3, 2, 2, 2]) == 0, 'Test5'

print("ОК")