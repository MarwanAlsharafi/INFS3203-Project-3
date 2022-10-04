import unittest 
from sms import addStudent, retrieveStudent, deleteStudent

class TestSms(unittest.TestCase):

    def test_addStudent(self):

        studentList = []
        addStudent(studentList, "osama", "24", "6009")
        actual = len(studentList) 
        expected = 1

        self.assertEqual(actual, expected)

    def test_retrieveStudent(self):

        studentList = []

        addStudent(studentList, "osama", "24", "6009")
        std = retrieveStudent(studentList, "6009")

        self.assertEqual(std["id"], "6009")
        self.assertEqual(std["age"], "24")
        self.assertEqual(std["name"], "osama")

    def test_deleteStudent(self):

        studentList = []

        addStudent(studentList, "osama", "24", "6009")
        deleteStudent(studentList, "6009")

        actual = len(studentList) 
        expected = 0

        self.assertEqual(actual, expected)
