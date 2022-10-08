from student_system import StudentSystem
from student import Student


def int_input(prompt):
    """Keep asking for an input until the user enters an integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer")


# add actions here
actions = {
    "1": "Add a new student.",
    "2": "Retrieve student.",
    "3": "Delete student.",
    "0": "Exit the system."
}


def main():
    student_system = StudentSystem()
    current_action = None

    print("Welcome to the Student Managment System")

    while current_action != "0":

        # add action handlers here
        if current_action == "1":
            print("adding student........................")

            name = input("Enter the student name: ")
            age = int_input("Enter the student age: ")
            id = int_input("Enter the student ID: ")

            new_student = Student(name, age, id)
            student_system.add_student(new_student)

            print(f"Student {name} added to the list.\n")

        elif current_action == "2":
            print("Retrieving student...................")

            id = int_input("Enter the student ID: ")

            std = student_system.find_student(id)

            print("Student retrieved...................")
            if std is None:
                print("No student found with that id.\n")
            else:
                print("Name:", std.name),
                print("Age:", std.age),
                print("Student ID:", std.id)

        elif current_action == "3":
            print("Deleting student.............")

            id = int_input("Enter student ID: ")

            student_deleted = student_system.delete_student(id)

            if student_deleted:
                print("Student deleted.")
            else:
                print("No student found with that id.")

        print("\n")
        for key, action in actions.items():
            print(key + ". " + action)

        current_action = input("\nChoose an action: ").strip()


if __name__ == "__main__":
    main()
