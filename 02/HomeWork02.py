# 1. Квадрат числа.
num_for_square = int(input("Введість число для приведенння до другого ступіня: "))

print("Число ",num_for_square,"після приведення до другого ступіня дорівнює:",
      num_for_square ** 2)

print("-" * 50)


# 2.“Середнє трьох чисел”
number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
number_3 = int(input("Введіть трете число: "))

print("Середнє арефметичне чисел",number_1 , number_2 ,number_3, "дорівнює: "
      , (number_1 + number_2 + number_3) / 3 )

print("-" * 50)


# 3.“Перетворення хвилин у години”
time_in_minutes = int(input("Введіть хвилини для розрахунку:"))

print("Розрахований час" , time_in_minutes // 60, "години",
      time_in_minutes - (60 * (time_in_minutes // 60)), "хвилин")

print("-" * 50)


# 4.“Розрахунок знижки”
item_price = int(input("Введість введіть ціну: "))
discount_percent = int(input("Введість введіть % знижки: "))

discount_amount = item_price * (discount_percent / 100)
final_price = item_price - discount_amount

print("При початковій ціні в:", item_price, "зі знижкою у:",
      discount_percent, "%", "сумма до сплати:", final_price )

print("-" * 50)


#5. “Остання цифра числа”
number_for_decomp = int(input("Введість число для визначення останьої цифри: "))
print("Остання цифра введеного числа: ", number_for_decomp % 10)


print("-" * 50)

#6. “Периметр прямокутника”
rect_height = int(input("Введіть довжину прямокутника: "))
rect_wide = int(input("Введіть ширину прямокутника: "))

print("Перемитер прямокутника з довжиною:", rect_height, "та шириною:", rect_wide, "дорівнює:",
      rect_height * 2 + rect_wide * 2)

print("-" * 50)

#7. Виведення числа в стовпчик
number_for_decomp_= int(input("Введіть число для виводу його у стовпчик: "))

print(number_for_decomp_ // 1000)
print((number_for_decomp_ // 100) % 10)
print((number_for_decomp_ // 10) % 10)
print(number_for_decomp_ % 10)