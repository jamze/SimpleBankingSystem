class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, I am {}!".format(self.name)


# name_input = str(input())

person1 = Person(input())

print(person1.greet())