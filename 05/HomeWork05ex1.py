# 5.1 Ім'я змінної
# Перевірити чи може рядок введений користувачем може бути назвою зімнної

import keyword as k

while True:
    variable_string = input("Введіть ім'я змінної для перевірки ")

    text_of_error = ("У назві для змінної {0} виявлена помилка.\n"
                     "Не можна використовувати {1} "
                     "для визначення імені змінної."
                     "Повторіть спробу ще раз!\n")

    if not variable_string[0].isdigit():
        if not k.iskeyword(variable_string) and variable_string.isidentifier():
            if any(symb.isupper() for symb in variable_string):
                error_det = "літери в UpperCase"
                print(variable_string + " False\n")
                print(text_of_error.format(variable_string, error_det))
            elif "__" in variable_string:
                error_det = "використувати більше одного _ підряд"
                print(variable_string + " False\n")
                print(text_of_error.format(variable_string, error_det))
            else:
                print(variable_string + " True")
        else:
            error_det = ("не можна використовувати зарезервовані"
                         " або заборонені символи у назві")
            print(variable_string + " False\n")
            print(text_of_error.format(variable_string, error_det))
    else:
        error_det = "числа на початку назви"
        print(variable_string + " False\n")
        print(text_of_error.format(variable_string, error_det))

    call_check = input("Хочете продовжити роботу?"
                       " (введіть y/yes) ").lower().strip()
    if call_check in ("y", "yes"):
        continue
    else:
        break
