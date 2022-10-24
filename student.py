import base64
import string
import random


def pass_random(pw_seed=None):
    """
    In order to be unit tested, a function needs to be deterministic, i.e.
    we need to know what the output of the function will be when we call it.

    In order to make the function deterministic, we generate random values
    from a seed instead, as long as the seed remains the same, the random
    values generated will be the same, allowing us to predict the output of the
    at the time of execution.

    Note that if the seed is None, a random seed will be used by python and
    the passwords generated will be completely random and unpredictable.
    """
    random.seed(pw_seed)
    password = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(password) for _ in range(8)))
    passEn = result_str.encode("utf-8")
    encoded = base64.b64encode(passEn)
    return encoded


class Student:
    def __str__(self):
        return f"{self.id}, {self.name}, {self.age}, {self.password}"

    def __eq__(self, student):
        return (self.id == student.id and self.name == student.name
                and self.age == student.age)

    def __init__(self, name, age, id, pw_seed=None):
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
        self.password = pass_random(pw_seed)
