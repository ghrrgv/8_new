#дан набор состоящий из букв Д И Н А. Из этого набора составляют слова длинной пять.
# Символы могут повторяться. Все возможные соова в алфавуитном порядке, нужно найти порядковый номер слова ДИАНА
# Пример:
# 1.AAAAA
# 2.AAAAД
# 3.AAAAИ
from itertools import *
for i in product('ДИНА', repeat = 5): # будет перебирать не в алфавитном порядке, а в том порядке в котором указано
    # тоесть начнёт с Д
    print(i) # тоесть, чтобы слова были в алфавитном порядке, нужно генерировать по АДИН, такое можно посмотреть в примере

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

num = 1 # счётчик
for i in product('АДИН', repeat = 5): # повторить 5 потому что пять ьукв в слове
    word = ''.join(i) # join - Объеденяет списки, т. е. вместо ('А', 'Д', 'И', 'Н') выедется АДИН, а ковычки это
# склеиватель, тоесть то тчо буедт между буквами.
    if word == 'ДИАНА':
        print(num, word)
    num+=1
