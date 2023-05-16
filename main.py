"""class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name, 'їсть')
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name, 'гавкає')
hotdog = Dog('bobik', 3, 'labrador')
print(hotdog.name, hotdog.breed, hotdog.age)
hotdog.eat()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name {self.name}, age {self.age}'
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + f' student_id {self.student_id}'
student1 = Student('Zahar', 45, '213512t123')
student2 = Student('Sanya', 20, '213512t124')

with open('info_student.txt', 'w') as file:
    file.write(str(student1))
    file.write(str(student2))
"""

import random

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        self.health = 100
        self.hunger = 0
        self.happiness = 100

    def grow(self):
        self.age += 1
        self.health -= random.randint(1, 5)
        self.hunger += random.randint(1, 5)
        self.happiness -= random.randint(1, 5)

    def eat(self):
        if self.hunger > 0:
            self.hunger -= random.randint(1, 5)
            self.happiness += random.randint(1, 3)
            print(f"{self.name} їсть")
        else:
            print(f"{self.name} не голодний")

    def play(self):
        if self.happiness > 0:
            self.happiness += random.randint(1, 5)
            self.hunger += random.randint(1, 3)
            print(f"{self.name} грається")
        else:
            print(f"{self.name} не хоче гратись")

    def __str__(self):
        return f"{self.name} це {self.species} і йому {self.age} років"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} додали до зоопарку")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} вигнали з зоопарку")
        else:
            print(f"{animal.name} не в зоопарку")

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def play_with(self):
        for animal in self.animals:
            animal.play()

    def grow_all(self):
        for animal in self.animals:
            animal.grow()

    def save_zoo_state(self, day):
        filename = f"Day_{day}.txt"
        with open(filename, "w") as file:
            file.write("Статистика:\n")
            for animal in self.animals:
                file.write(str(animal) + "\n")

zoo = Zoo()

lion = Animal("Лев", "Бобік", 5)
elephant = Animal("Слон", "Арчі", 3)
giraffe = Animal("Жираф", "Лео", 2)

zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(giraffe)

for day in range(1, 11):
    print(f"Day {day}:")
    zoo.feed_all()
    zoo.play_with()
    zoo.grow_all()
    zoo.save_zoo_state(day)
    print()

