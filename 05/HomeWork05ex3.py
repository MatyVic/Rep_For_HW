# 5.3. hashtag
import string

while True:
    str_to_hashtag = input("Введіть фразу для перетворення ")
    new_str = ""

    for ch in str_to_hashtag:
        if ch in string.punctuation:
            ch = ""
        else:
            new_str += ch

    print("#" + new_str[:140].title().replace(" ", ""))

    call_check = input("Хочете продовжити роботу?"
                       " (введіть y/yes) ").lower().strip()
    if call_check in ("y", "yes"):
        continue
    else:
        break

