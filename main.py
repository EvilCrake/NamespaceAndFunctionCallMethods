# a = ('Hello')
# bb = input('Enter ur name: ')
#
# def test(a, b):
#     a = ('Hello, ')
#     b = {bb}
#     print(a, bb)
#
# test(a, bb)
#
# aa = int(input('How are u? Answer: 1- Nice, 2- Sad, 3- So-so.'))
# ab = ('Nice!')
# ad = ('No more sadness!')
# ac = ('Its gonna be okay!')
# if aa == 1:
#     print(ab)
# if aa == 2:
#     print(ad)
# if aa == 3:
#     print(ac)
# def test2(aa, ab, ac):
#     print(aa, ab, ac)
#
# test2(aa, ab, ac)
# print('Good bye!')

# Пространство имен и способы вызова функции

def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    return same_words


# Пример использования функции
result0 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result0)
print(result1)


