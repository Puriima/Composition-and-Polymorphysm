#1. **Создание базового класса Animal**

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

# 2. **Реализация наследования с подклассами Bird, Mammal, и Reptile**

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Tweet'")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Woof'")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says 'Hiss'")

# 3. **Демонстрация полиморфизма**

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# 4. **Использование композиции для создания класса Zoo**

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

#5. **Создание классов для сотрудников ZooKeeper и Veterinarian**

class ZooKeeper:
    def feed_animal(self, animals):
        for animal in animals:
            print(f"Feeding {animal.name}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Healing {animal.name}")

#**Дополнительно: Сохранение и загрузка информации о зоопарке**

#Для этого, предположим, что мы будем сериализовать и десериализовать объекты с помощью модуля `pickle`.

import pickle

def save_zoo(zoo, filename="zoo.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)
        print(f"Zoo saved to {filename}.")

def load_zoo(filename="zoo.pkl"):
    try:
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        return zoo
    except FileNotFoundError:
        print(f"No saved zoo found with the name {filename}. Starting a new zoo.")
        return Zoo()

# Пример использования:
zoo = Zoo()
zoo.add_animal(Bird("Parrot", 3))
zoo.add_staff(ZooKeeper())

save_zoo(zoo)
loaded_zoo = load_zoo()