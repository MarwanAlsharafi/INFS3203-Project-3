from student import Student


class StudentSystem:

    def __init__(self):
        self.students: dict(int, Student) = {}

    def add_student(self, student: Student):
        """Adds a student to the system"""
        if type(student) != Student:
            raise TypeError("student should be object of class Student.")

        self.students[student.id] = student

    def list_students(self):
        """Lists the students in the system"""
        if len(self.students) == 0:
            print("There are no students in the list currently.")
        else:
            for student in self.students.values():
                print(
                    f'Name: {student.name}, '
                    f'Age: {student.age}, '
                    f'Student ID: {student.id}'
                    )

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

    def export_students(self, filename: str = "students.csv"):
        if filename[-4:] != ".csv":
            filename = filename + ".csv"

        with open(filename, 'w') as f:
            f.write("id, name, age, password\n")
            for student in self.students.values():
                f.write(str(student) + "\n")

        return filename
