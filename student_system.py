from student import Student
import csv


class StudentSystem:

    def __init__(self):
        self.students: dict(int, Student) = {}

    def add_student(self, student: Student):
        """Adds a student to the system"""
        if type(student) != Student:
            raise TypeError("student should be object of class Student.")
        if student.id in self.students:
            raise ValueError("Student with ID: " +
                             str(student.id) + "already exists")

        self.students[student.id] = student

    def find_student(self, id: int):
        """
        Finds a student based on the id of the student.
        If no student is found returns None
        """
        if id in self.students:
            return self.students[id]
        return None

    def delete_student(self, id: int):
        """
        Deletes the student with the given id.
        True is returned if deletion is successful.
        If the student is not found or deletion fails, False is returned.
        """
        if id in self.students:
            del self.students[id]
            return True
        return False

    def import_students(self, filename: str = "students.csv"):
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                
                new_student = Student(row[1].strip(), int(row[2]), int(row[0]))
                self.add_student(new_student)
    
    def export_students(self, filename: str = "students.csv"):
        if filename[-4:] != ".csv":
            filename = filename + ".csv"

        with open(filename, 'w') as f:
            f.write("id, name, age, password\n")
            for student in self.students.values():
                f.write(str(student) + "\n")

        return filename
