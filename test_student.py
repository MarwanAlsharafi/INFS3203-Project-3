from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test_negative_id_exception(self):
        """Checks that negative id results in a TypeError"""
        with self.assertRaises(TypeError):
            Student("Asmar", 23, -1)

    def test_negative_age_exception(self):
        """Checks that negative age results in a TypeError"""
        with self.assertRaises(TypeError):
            Student("Asmar", -1, 1)

    def test_no_id_exception(self):
        """
        Checks that creating a student without an id results in a TypeError
        """
        with self.assertRaises(TypeError):
            Student("Asmar", 23)

    def test_no_name_exception(self):
        """
        Checks that creating a student without a name results in a TypeError
        """
        with self.assertRaises(TypeError):
            Student(age=23, id=1)

    def test_no_age_exception(self):
        """
        Checks that creating a student without an age results in a TypeError
        """
        with self.assertRaises(TypeError):
            Student("Asmar", id=1)

    def test_wrong_id_type_exception(self):
        """Checks that not having id as an integer results in a TypeError"""
        with self.assertRaises(TypeError):
            Student("Asmar", 23, "1")

        with self.assertRaises(TypeError):
            Student("Asmar", 23, True)

        with self.assertRaises(TypeError):
            Student("Asmar", 23, 1.0)

    def test_wrong_age_type_exception(self):
        """Checks that not having age as an integer results in a TypeError"""
        with self.assertRaises(TypeError):
            Student("Asmar", "23", 1)

        with self.assertRaises(TypeError):
            Student("Asmar", False, 1)

        with self.assertRaises(TypeError):
            Student("Asmar", 23.0, 1)

    def test_wrong_name_type_exception(self):
        """Checks that not having name as a string results in a TypeError"""
        with self.assertRaises(TypeError):
            Student(True, 23, 1)

        with self.assertRaises(TypeError):
            Student(5, 23, 1)

        with self.assertRaises(TypeError):
            Student(['A', 's', 'm', 'a', 'r'], 23, 1)
