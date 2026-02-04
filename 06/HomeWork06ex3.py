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


    ind_1 = string.ascii_letters.index(my_str[0])
    ind_2 = string.ascii_letters.index(my_str[-1])

    #print(string.ascii_letters[ind_1:ind_2 + 1])
