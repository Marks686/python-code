import inspect


class Dog:
    pass

dahuang = Dog()
# print(inspect.isclass(Dog))
# print(inspect.isclass(dahuang))
# print(type(dahuang))


print(isinstance(dahuang, Dog))