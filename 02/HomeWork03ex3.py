# 3.3. Розділити один список на два списки
my_list = list(input("Введіть ваш список:"))

print("Довжина списку", len(my_list))
lst_len = round(len(my_list) / 2 + 0.001)

print("Перетворюємо вихідний список на список "
      "у якомубуде два вкладені списки:")

lst_result = [my_list[:lst_len], my_list[lst_len:]]

print("Результат роботи програми:")
print(lst_result)
