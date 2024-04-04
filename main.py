"""Metaclass"""


class MetaClass(type):
    """Metaclass"""
    def __new__(cls, name, bases, attrs):
        print(f'Hello my new class {name}')
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MetaClass):
    """New class"""
    pass


class MyNextClass(metaclass=MetaClass):
    """New class"""
    pass
