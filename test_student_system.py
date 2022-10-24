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

    def test_import_student_works(self):
        """
        Checks that import student works
        """

        student_system = StudentSystem()
        student_system.import_students("students_test.csv")

        self.assertEqual(student_system.students[1], Student('Asmar', 23, 1))
        self.assertEqual(student_system.students[2], Student('Huzaifa', 23, 2))
        self.assertEqual(student_system.students[3], Student('Osama', 24, 3))
        self.assertEqual(student_system.students[4], Student('Ahmed', 23, 4))
        self.assertEqual(student_system.students[5], Student('Marwan', 23, 5))

    def test_import_student_file_nonexistant(self):
        """
        Checks if the import student CSV file exists or not
        """
        student_system = StudentSystem()

        with self.assertRaises(FileNotFoundError):
            student_system.import_students("idk.csv")

    def test_import_student_empty_file(self):
        """
        Checks that import student csv file is empty or not
        """
        student_system = StudentSystem()
        student_system.import_students("empty_test.csv")
        self.assertEqual(len(student_system.students), 0)

    def test_export_student_creates_empty_file(self):
        """
        Checks that export student works even if student list is empty
        and that the header row is generated
        """
        student_system = StudentSystem()
        filename = student_system.export_students()
        with open(filename) as f:
            lines = f.readlines()
            # Header row exists
            self.assertEqual(lines[0].strip(), "id, name, age, password")
            # File data is empty
            self.assertEqual(len(lines), 1)

    def test_export_student_creates_csv_file(self):
        """
        Load some students into the system and check that export student works
        """
        student_system = StudentSystem()
        student_system.add_student(
            Student("Asmar", 23, 1, "pw_seed_for_unit_test_1"))
        student_system.add_student(
            Student("Huzaifa", 23, 2, "pw_seed_for_unit_test_2"))
        student_system.add_student(
            Student("Osama", 24, 3, "pw_seed_for_unit_test_3"))
        student_system.add_student(
            Student("Ahmed", 23, 4, "pw_seed_for_unit_test_4"))
        student_system.add_student(
            Student("Marwan", 23, 5, "pw_seed_for_unit_test_5"))
        filename = student_system.export_students()
        with open(filename) as f:
            lines = f.readlines()
            # Header row exists
            self.assertEqual(lines[0].strip(), "id, name, age, password")
            self.assertEqual(lines[1].strip(),
                             "1, Asmar, 23, b'SnhBMG9OTm8='")
            self.assertEqual(lines[2].strip(),
                             "2, Huzaifa, 23, b'QTJnU1Q2c1A='")
            self.assertEqual(lines[3].strip(),
                             "3, Osama, 24, b'WWlqc1loc1Q='")
            self.assertEqual(lines[4].strip(),
                             "4, Ahmed, 23, b'UjhJU01rQ3A='")
            self.assertEqual(lines[5].strip(),
                             "5, Marwan, 23, b'eVUyd0xuR0Q='")
            # File has header row + 5 data row
            self.assertEqual(len(lines), 6)
