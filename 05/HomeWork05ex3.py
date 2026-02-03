# 5.3. hashtag
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

import string

while True:
    str_to_hashtag = input("Введіть фразу для перетворення ").title()
    new_str = ""

    for ch in str_to_hashtag:
        if ch in string.punctuation or ch == " ":
            ch = ""
        else:
            new_str += ch

    print("#" + new_str[:139])

    call_check = input("Хочете продовжити роботу?"
                       " (введіть y/yes) ").lower().strip()
    if call_check not in ("y", "yes"):
        break
