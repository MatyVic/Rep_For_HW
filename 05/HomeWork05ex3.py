# 5.3. hashtag
import string

str_to_hashtag = input("Введіть фразу для перетворення ")
new_str = ""

for ch in str_to_hashtag:
    if ch in string.punctuation:
        ch = ""
    else:
        new_str += ch

print("#" + new_str[:140].title().replace(" ", ""))
