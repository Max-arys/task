""" Декоратор property"""


class Person:
    humans = 'human'

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)
    name = property(get_name, set_name)


class Persone:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Persone('Сергей', 20)
p.name = 'Tom'
p.old = 6
print(p.name, p.old)
