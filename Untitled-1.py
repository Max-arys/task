"""Написать функцию, которая проверяет что все открытые скобки были закрыты."""

"""хорошие примеры:

*   ((1, 2)(3))
*   ((((10)(a))(foo) bar)())

плохие примеры

*   (()
*   ((()())"""

a = '((1, 2)(3))'
b = '((((10)(a))(foo) bar)())'
c = '((,)'
d = '(p(j(3)j(h))'


def parentheses_counter(x):
    if x.count('(') == x.count(')'):
        print(True)
    else:
        print(False)


parentheses_counter(a)
parentheses_counter(b)
parentheses_counter(c)
parentheses_counter(d)
