# 4.2. Знайти суму елементів із парними індексами
my_lst = [1, 3, 5]
exercise_res = 0

if not len(my_lst) == 0:
    # За допомогою for перебираємо список і складаємо парні елементи
    for item_id, item in enumerate(my_lst):
        if item_id % 2 == 0:
            exercise_res += item
    else:
        exercise_res *= my_lst[-1]

# Виводимо результат програми
print(exercise_res)
