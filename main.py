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

word = "Join"
word0 = "game"
word1 = "type"

def single_root_words(root_word, *other_words):
    same_words = []
    same_words.append(root_word)
    same_words.extend(other_words)

    for word in same_words:
        if " " not in word:
            print(word)
    return same_words

result = single_root_words(word, word0, word1)
print("Результат функции:", result)


