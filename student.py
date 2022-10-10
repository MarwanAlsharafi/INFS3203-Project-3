class Student:
    def __str__(self):
        return f"{self.id}, {self.name}, {self.age}"

    def __init__(self, name, age, id):
        if type(name) != str:
            raise TypeError("Name should be a string.")
        if type(age) != int:
            raise TypeError("Age should be an int.")
        if type(id) != int:
            raise TypeError("ID should be an int.")
        if age < 0:
            raise TypeError("Age should not be negative")
        if id < 0:
            raise TypeError("ID should not be negative")
        self.name = name
        self.age = age
        self.id = id
