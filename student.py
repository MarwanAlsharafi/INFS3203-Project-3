import base64
import string
import random


def pass_random():
    password = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(password) for i in range(8)))
    passEn = result_str.encode("utf-8")
    encoded = base64.b64encode(passEn)
    return encoded


class Student:
    def __str__(self):
        return f"{self.id}, {self.name}, {self.age}, {self.password}"

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
        self.password = pass_random()
