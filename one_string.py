# Если создаваемая последовательность не будет изменяться в будущем,
# то лучше создать tuple для экономии ресурсов машины.
# Так же в переменные лучше записывать генераторы 'generator object':
# используем '()' вместо '[]'
"""unpacking"""
# map применяет функцию к переданной последовательности
x, y, z = map(int, input().strip().split())
print(x, y, z, '-unpacking')

# reduce применяет функцию к последовательности,
# сводит процес к единственному результату
from functools import reduce

x, y, z = map(int, input().strip().split())
value = reduce((lambda a, b: a + b), (x, y, z), 0)
print(value, '-reduce')


"""Comprehensions"""
names = ["Христофор", "Адемар", "Тэя", "Стефания", "Архип"]
names_starts_a = [name for name in names if name.startswith("А")]
print(names_starts_a, '-Comprehensions')

# filter принимает обработчик возвращающий True или False и последовательность
# lambda a,b; a + b == lambda(a, b):
                        # return a + b
# пример:
# >>>(lambda x, y: x+y)(5, 7)
# >>>12
names = ["Христофор", "Адемар", "Тэя", "Стефания", "Архип"]
names_starts_with_a = list(filter(lambda name: name.startswith("А"), names))
print(names_starts_a, '-filter')


"""copying"""
# слайс создает новую последовательность
indexes = [1, 2, 3]
another_indexes = indexes[:]


"""if short"""
# Вместо or скобки
name = 'Тэя'
if name in ("Христофор", "Адемар", "Тэя"):
    print(name, '-()')

# проверяем все ли элементы последовательности возвращают True,
# вместо and
a = (1, 0, 5)
if all(a):
    print("ok", '-all', end=' ')
print(1, '-all')

if all([i >= 0 for i in a]):
    print("ok", '-all', end=' ')
print(2, '-all')

# проверяем есть ли в последовательности элемент возвращающий True,
# вместо or
print(any(a), '-any')

# тернарный оператор
print('Hello' if all(a) else 'Good bye', '-ternary')
