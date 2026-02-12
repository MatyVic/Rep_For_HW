# ДЗ 8.2. Паліндром
import string


def is_palindrome(text):
    my_text = text.replace(" ", "").lower()
    my_text = "".join(ch for ch in my_text if ch not in string.punctuation)

    return my_text == my_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
