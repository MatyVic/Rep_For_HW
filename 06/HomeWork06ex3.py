# ДЗ 6.3. Добуток чисел

exit_check = "y"
while exit_check in ["y", "yes", "т", "так"]:

    my_num = int(input("Введіть число: "))

    while my_num > 9:
        res = 1
        for item in str(my_num):
            res *= int(item)
        my_num = res

    print(my_num)
    exit_check = input("Продовжити? (y/yes/т/так) ").lower()
