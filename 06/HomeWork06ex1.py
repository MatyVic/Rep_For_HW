# ДЗ 6.1. Діапазон букв

import string

exit_check = "y"
while exit_check in ["y", "yes", "т", "так"]:
    my_str = input("Введіть проміжок через - ").replace("-", "")

    result = ""
    fist_asc = ord(my_str[0])
    last_asc = ord(my_str[1])

    start, end = sorted([fist_asc, last_asc])
    for asc in range(start, end + 1):
        if chr(asc) not in string.punctuation:
            result += chr(asc)

    print(result)
    exit_check = input("Продовжити? (y/yes/т/так) ").lower()
