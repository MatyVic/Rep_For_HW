# 6.2. Конвертер із числа в дату

time_in_sec = int(input("Введіть секунди для розрахунку:").strip())

first_rule = (2, 3, 4)
second_rule = (12, 13, 14)

if time_in_sec < 8640000:
    days = time_in_sec // 86400
    hours = str((time_in_sec % 86400) // 3600).zfill(2)
    minutes = str((time_in_sec % 3600) // 60).zfill(2)
    seconds = str(time_in_sec % 60).zfill(2)

    if days % 10 == 1 and days % 100 != 11:
        paste_word = "день"
    elif days % 10 in first_rule and days % 100 not in second_rule:
        paste_word = "дні"
    else:
        paste_word = "днів"

    print(f"{days} {paste_word}, {hours}:{minutes}:{seconds}")

else:
    print("Велике число")
