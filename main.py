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
    def __init__(self, species, name, age, health, hunger, happiness)
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
    def grow(self):
        self.age += 1
        self.health = random.randint(0, 10)
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
    def eat(self):
        if self.hunger >= 6:
            self.health += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
            self.hunger -= random.randint(5, 7)
        else:
            print(self.name, 'голодний')
    def play(self):
        if self.happiness >= 5:
            self.health += random.randint(0, 5)
            self.hunger += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
        else:
            print(self.name, 'does not want to play')
    def __str__(self):
        return f'{self.species} - {self.name} ({self.age} years old)\n' \
               f'Health: {self.health}\nHunger: {self.hunger}\nHappiness: {self.happiness}\n'

class Zoo:
    def __init__(self):
        super().__init__()
        self.animals = []

#Simulating 10 day
for i in range(1, 11):
    print(f'Day {i}')
    save_zoo_state(zoo, i)
    zoo.feed_all()
    zoo.play_with(zoo.animals[random.randint(0, len(zoo.animals) - 1)])
    zoo.geow_all()
    print(zoo)
    print('\n')
print('Simulation finished.')