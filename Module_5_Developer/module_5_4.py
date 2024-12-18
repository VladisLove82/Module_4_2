class House:
    def __new__(cls, *args, **kwargs):
        cls.houses_history = []
        print(args)
        print(**kwargs)
        return object.__new__(cls)

    def __init__(self):

    def __del__(self):
        return "<название> снесён, но он останется в истории"


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)