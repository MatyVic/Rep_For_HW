# ДЗ 4.3. Список із 3 елементів
import random as rnd

my_lst = []
# Наповнюємо список випадкової довжини випадковими елементами
for i in range(rnd.randint(3, 10)):
    my_lst.append(rnd.randint(0, 25))

print("Створений список:", my_lst)
print("Результуючий список з трьох елементів",
      [my_lst[0], my_lst[2], my_lst[-2]])
