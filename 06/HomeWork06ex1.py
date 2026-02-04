# ДЗ 6.1. Діапазон букв

import string

exit_check = "y"
while exit_check in ["y", "yes", "т", "так"]:
    my_str = input("Введіть проміжок через - ")

    ind_1 = string.ascii_letters.index(my_str[0])
    ind_2 = string.ascii_letters.index(my_str[-1])

    print(ind_1, ind_2)


    exit_check = input("Продовжити? (y/yes/т/так) ").lower()
