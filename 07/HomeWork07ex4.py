# ДЗ 7.4. Пошук спільних елементів

def common_elements():
    set_1 = {item for item in range(100) if item % 3 == 0}
    set_2 = {item for item in range(100) if item % 5 == 0}

    return set_1.intersection(set_2)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
