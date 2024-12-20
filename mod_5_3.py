class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self,new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            return new_floor
        else:
            return "Такого этажа не существует"
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __it__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        else:
            self.number_of_floors += value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return House (self.number_of_floors + value.number_of_floors)
h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)
# print(h1.go_to(11))
# print(h2.go_to(20))
print(h1)
print(h2)
# print(len((h1)))
# print(len((h2)))
print(h1 == h2)
print(h1)
print(h1 == h2)
print(h1)
print(h2)
print(h1>h2)
print(h1>=h2)
print(h1<h2)
print(h1>=h2)
print(h1!=h2)
print(h1+h2)
