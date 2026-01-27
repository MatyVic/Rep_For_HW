My_list = [1]

if 0 == len(My_list) <= 1:
    print("Результат заміни елемента:", My_list)
else:
    last_element = My_list.pop(-1)
    My_list.insert(0, last_element)
    print("Результат заміни елемента:", My_list)
