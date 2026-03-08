# student list game

students = [
    {"username": "Nafim", "age": 22, "grade": "A"},
    {"username": "Ahnaf", "age": 21, "grade": "B+"},
    {"username": "Manna", "age": 23, "grade": "A-"},
    {"username": "Rahim", "age": 20, "grade": "B"},
    {"username": "Karim", "age": 24, "grade": "A"},
    {"username": "Sami", "age": 22, "grade": "B+"},
    {"username": "Ayan", "age": 21, "grade": "A-"},
    {"username": "Arif", "age": 23, "grade": "B"},
    {"username": "Tanmoy", "age": 20, "grade": "A"},
    {"username": "Sakib", "age": 22, "grade": "B+"}
]

def add_student():
    username = input("enter username: ")
    age = input("enter age: ")
    grade = input("enter grade point: ")

    student = {
        "username" : username,
        "age" : age,
        "grade" : grade
    }

    students.append(student)

    print("student name has been added.\n")

def show_students():
    if not students:
        print("No students is in the system.\n")
        return
    for index, student in enumerate(students, start = 1):
        print(f"{index}. Name:{student['username']}, Age: {student['age']}, Grade: {student['grade']}")
    print()
def search_student():
    search_username = input("enter username to search: ")

    for student in students:
        if student["username"].lower() == search_username.lower():
            print(f"Found: {student['username']} - Age: {student['age']}, Grade: {student['grade']}\n")
            return
    print("student is not found!\n")

def del_student():
    search_username = input("enter username")

    for index, student in enumerate(students):
        if student['username'].lower() == search_username.lower():
            del students[index]
            print("student username is deleted.\n")
            return
    print("student is not found.\n")
print("1. adding students.")
print("2. show students.")
print("3. search students.")
print("4. deleting students")

choice = input("choose from on of the above.")

if choice == "1":
    add_student()
elif choice == "2":
    show_students()
elif choice == "3":
    search_student()
elif choice == "4":
    del_student()
else:
    print("Invalid request")
