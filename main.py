class Animal:
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