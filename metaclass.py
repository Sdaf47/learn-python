#!/usr/bin/env python
# coding: utf8
class ObjectCreator(object):
    def __init__(self):
        """
        Создаем объект

        """
        pass


def choose_class(name):
    """
    Фабрика классов
    
    Принимает имя класса, возвращает либо конкретный класс, либо абстрактный, если конкретного нет
    
    :param name: 
    :return: 
    """
    if name == 'specific':
        class Specific(object):
            pass

        return Specific
    else:
        class Abstract(object):
            pass

    return Abstract


class Parent(type):
    __metaclass__ = type
    pass


class Child:
    __metaclass__ = Parent


def meta_decorator(class_name, class_parents, class_attr):
    attrs = dict(('__' + name, value) for name, value in class_attr.items() if not name.startswith('__'))
    return type(class_name, class_parents, attrs)


class MetaDecorator(type):

    def __init__(cls, name, bases, dct):

        attrs = dict(('__' + name, value) for name, value in dct.items() if not name.startswith('__'))

        return super(MetaDecorator, cls).__init__(cls, name, bases, attrs)


if __name__ == '__main__':
    my_object = ObjectCreator()
    print("Объект", my_object)

    SpecificClass = choose_class('specific')
    print("Класс из функции-фабрики", SpecificClass)

    GenChild = type("GenChild", (), {'branch': int(), 'user': "anonymous"})
    print("Класс из генератора классов", GenChild)

    ChildInstance = GenChild()
    print("Объект из сгенерированного класса", ChildInstance, "со свойством user", ChildInstance.user)

    print("Мета-класс", ChildInstance.__class__.__class__)

    print("С помощью атрибута __meta__:", Child.__class__)

    PrivateClass = meta_decorator('PrivateClass', (), {'prop1': 1, 'prop2': 2})
    private_object = PrivateClass()
    print("Объект класс созданного кастомным мета-классом", getattr(private_object, '__prop1'))
