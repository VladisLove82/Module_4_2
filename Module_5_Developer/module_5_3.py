class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не сущесвует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.name == other.number_of_floors

    def __lt__(self, other):
        return self.name < other.number_of_floors

    def __le__(self, other):
        return self.name <= other.number_of_floors

    def __gt__(self, other):
        return self.name > other.number_of_floors

    def __ge__(self, other):
        return self.name >= other.number_of_floors

    def __ne__(self, other):
        return self.name != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            return self






h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print()

# Задача "Магические задания"
'''Добалено втрорая часть кода 
для продолжения первой задачи'''

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print()

#Задача "Нужно больше этажей"
'''Добалено третья часть кода 
для продолжения первой и второй задачи'''
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

