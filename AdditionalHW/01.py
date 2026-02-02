# Написати програму, яка просить ввести 4 числа – кількість днів, годин,
# хвилин і секунд. Програма виводить цей час у секундах.
# Введення даних зробити у 4-х окремих інпутах.

while True:
    days_counter = int(input("Введіть кількість днів "))
    hours_counter = int(input("Введіть кількіть годин "))
    minutes_counter = int(input("Введіть кількість хвилин "))
    seconds_counter = int(input("Введіть кількість секунд "))

    print("Результат роботи програми")
    print("Переведення " + str(days_counter) + " днів "
          + str(hours_counter) + " годин " + str(minutes_counter) + " хвилин "
          + str(seconds_counter) + " секунд в секунди дорівнює:")

    print(str(seconds_counter + (minutes_counter * 60) + (hours_counter * 3600)
          + (days_counter * 86400)) + " секунд")

    cont_chek = input("Продовжити роботу програми ? (y/n) ").lower()
    if cont_chek in ["y"]:
        continue
    elif cont_chek in ["n"]:
        break
