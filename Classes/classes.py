# Classes
class Person():
    age = 0  # class attributes
    name = "Doe"

    def __init__(self, name, age):
        # this always runs when you make a new instance
        print("A new person named", name, "has been added")
        self.name = name
        self.age = age
        self.apples = 0
    def say_hi(self):
        print(self.name, "say Hi!")

class Student(Person):
    # Student inherits all of the methods and attributes of Person
    def __init__(self, name, age, ):
        super().__init__(name, age)  # runs the parent constructor
        print("A new student named", name, "has been added")
        self.name = name
        self.age = age
        self.apples = 2

    def give_apple(self, teacher):
        if self.apples > 0:
            self.appples -= 1
            teacher.apples += 1
            print(self.name, "gave an apple to", teacher.name)
        else:
            print(self.name, "is out of apples")

class Teacher(Person):
    def eat_apples(self):
        if self.apples > 0:
            self.apples -= 1
            print(self. name, "ate an apple, Yum!")
        else:
            print(self.name, "is out of apples. :(")

person = Person("Ava", 17)  # created an instance of the Person class
print(person)  # the object itself
print(person.age)  # use dot notation to access or change attributes
person.age = 18  # changed it for this instance only
print(person.age)
print(Person.age)  # this prints the CLASS attribute

teacher = Teacher("Cal", 66)

student = Student("Bev", 16)
student.say_hi()
student.give_apple(teacher)
student.give_apple(teacher)
student.give_apple(teacher)
print(teacher.apples)