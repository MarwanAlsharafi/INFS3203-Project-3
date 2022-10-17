from unittest import TestCase
from student import Student
import base64


def isBase64(s):
    """The string is being decoded and the encoded for a comparison
    and if it is unsucessful it returns false"""
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


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

    def test_password_is_generated(self):
        """Checks that student has a password and it is encoded in base64"""
        student = Student("Asmar", 23, 1)
        self.assertIsNotNone(student.password)
        self.assertTrue(isBase64(student.password))

    def test_password_can_be_seeded(self):
        """
        Checks that if a student password is generated using a seed, it is
        predictable. As long as the seed is pw_seed_for_unit_test, the
        password generated should be PGQoAG3J, this might break in future
        versions of python if the random library changes.
        """
        student = Student("Asmar", 23, 1, "pw_seed_for_unit_test")
        pregenerated_password = b"PGQoAG3J"
        b64_encoded = b'UEdRb0FHM0o='
        self.assertEqual(b64_encoded, student.password)
        self.assertEqual(pregenerated_password,
                         base64.b64decode(student.password))
