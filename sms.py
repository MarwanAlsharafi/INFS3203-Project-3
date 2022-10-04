def addStudent(studentList, name, age, id):
    studentList.append({"name":name, "age":age, "id":id})

def retrieveStudent(studentList, id):
    for student in studentList:
        if id == student["id"]:
            return student

def deleteStudent(studentList, id):
    for i in range(len(studentList)):
        if id == studentList[i]["id"]:
            del studentList[i]
    return studentList

def main():

    students = []
    state = ""

    print("Welcome to the Student Managment System!!\n\n")

    while state != "4":

        if state == "1":
            print(students)
            print("adding student........................\n")

            name = input("Enter the student name: ")
            age = input("Enter the student age: ")
            id = input("Enter the student ID: ")

            addStudent(students, name, age, id)

            print("Student added to the list.\n")
            print(students)

        elif state == "2":
            print("Retrieveing student...................\n")

            id = input("Enter the student ID: ")

            std = retrieveStudent(students, id)

            print("Student retrieved...................\n")
            print("Name: " + std["name"]),
            print("Age: " + std["age"]),
            print("Student ID: " + std["id"])

        elif state == "3":
            print(students)
            print("Deleting student.............\n")

            id = input("Enter student ID: ")

            deleteStudent(students, id)

            print("Student deleted.")
            print(students)

        print("\n1. Add a new student.\n2. Retrieve student.\n3. Delete student.\n4. Exit the system.\n")

        state = input("choose your action: ")

main()