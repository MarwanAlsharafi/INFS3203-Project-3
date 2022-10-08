from unittest import TestCase
from student_system import StudentSystem, Student


class TestStudentSystem(TestCase):
    def test_add_student_success(self):
        """
        Checks that adding a student works without error
        Accesses system internals to ensure student was added.
        """
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertIs(student_system.students[1], test_student)

    def test_find_student_success(self):
        """
        Checks that finding a student produces works without error
        """
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertIs(student_system.find_student(1), test_student)

    def test_delete_student_success(self):
        """
        Checks that deleting a student produces works without error
        delete_student() should return True if deletion was successful
        Accesses system internals to ensure student was deleted.
        """
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertTrue(student_system.delete_student(1))
        self.assertFalse(test_student.id in student_system.students)

    def test_add_student_exception(self):
        """
        Checks that adding a student incorrectly results in a TypeError
        """
        student_system = StudentSystem()

        with self.assertRaises(TypeError):
            student_system.add_student("Asmar", 23, 1)

    def test_find_student_not_exists(self):
        """
        Checks that finding a student with a non-existent id returns None
        """
        student_system = StudentSystem()

        self.assertEqual(student_system.find_student(1), None)

        test_student = Student("Asmar", 23, 1)
        student_system.add_student(test_student)

        self.assertEqual(student_system.find_student(0), None)

    def test_delete_student_not_exists(self):
        """
        Checks that deleting a student with a non-existent id returns False
        """
        student_system = StudentSystem()

        self.assertFalse(student_system.delete_student(1))

        test_student = Student("Asmar", 23, 1)
        student_system.add_student(test_student)

        self.assertFalse(student_system.delete_student(0))
