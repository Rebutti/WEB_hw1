class Meta(type):
    # тут должно быть ваше решение
    class_number = -1

    def __new__(cls, class_name, parents, attributes: dict):
        print('Creating class', class_name)
        cls.class_number = cls.class_number + 1
        print(f"class_number = ", cls.class_number)
        attributes["class_number"] = cls.class_number
        # Here we could add some helper methods or attributes to c
        c = type(class_name, parents, attributes)
        return c


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1('a'), Cls2('b')
assert (a.class_number, b.class_number) == (0, 1)
