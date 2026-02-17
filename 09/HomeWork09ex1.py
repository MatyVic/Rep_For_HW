# ДЗ 9.1. Визначити популярність певних слів у тексті
import string


def popular_words(text, words):

    for item in string.punctuation:
        text = text.replace(item, '')

    text = text.lower()
    text_words = text.split()

    res = {}
    for item in words:
        res[item] = text_words.count(item.lower())

    return res


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
