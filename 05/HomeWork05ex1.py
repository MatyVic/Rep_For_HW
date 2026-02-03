# 5.1 Ім'я змінної
# Перевірити чи може рядок введений користувачем може бути назвою змінної

import keyword as k

while True:
    variable_string = input("Введіть ім'я змінної для перевірки ")

    text_of_error = ("У назві для змінної {0} виявлена помилка.\n"
                     "Не можна {1} для визначення імені змінної."
                     "Повторіть спробу ще раз!\n")

    if not variable_string[0].isdigit():
        if not k.iskeyword(variable_string) and variable_string.isidentifier():
            if any(symb.isupper() for symb in variable_string):
                error_det = "використовувати літери в UpperCase"
                print(variable_string + " False\n")
                print(text_of_error.format(variable_string, error_det))
            elif set(variable_string) == {"_"} and len(variable_string) > 1:
                error_det = "використовувати тільки _ "
                print(variable_string + " False\n")
                print(text_of_error.format(variable_string, error_det))
            else:
                print(variable_string + " True")
        else:
            error_det = ("використовувати зарезервовані"
                         " або заборонені символи у назві")
            print(variable_string + " False\n")
            print(text_of_error.format(variable_string, error_det))
    else:
        error_det = "використовувати числа на початку назви"
        print(variable_string + " False\n")
        print(text_of_error.format(variable_string, error_det))

    call_check = input("Хочете продовжити роботу?"
                       " (введіть y/yes) ").lower().strip()
    if call_check not in ("y", "yes"):
        break
