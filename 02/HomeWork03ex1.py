#   3.1. Найпростіший калькулятор
#   Просимо кориустувача ввести операцію
calc_operation = input("Введіть операцію (+, -, *, /)")

#   Просимо користувача вести числа для викоання арефметичної операції
number_1 = input("Ведіть перше число: ")
number_2 = input("Ведіть друге число: ")

#   Перевіряємо введений текст на можливість перетворення у int
if number_1.isdigit() and number_2.isdigit():
    number_1 = float(number_1)
    number_2 = float(number_2)

#   Виконуємо операції
    if calc_operation == "+":
        print("Результат суми двох чисел:", number_1 + number_2)
    elif calc_operation == "-":
        print("Результат віднімання двох числех:", number_1 - number_2)
    elif calc_operation == "*":
        print("Результат множення двох чисел:", number_1 * number_2)
    elif calc_operation == "/":
        if number_2 == 0:
            print("Ви намагалися виконати ділення на 0")
        else:
            print("Результат операції ділення дорівнює:", number_1 / number_2)
    else:
        print("Перевірте парвильність вводу операції дозволені "
              "тільки прості арефметичні операції (+, -, *, /)")
else:
    print("Ви ввели неправльне перше число: ", number_1, number_2)
