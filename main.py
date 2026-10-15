import json


# Save new students 1
def student_save():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        students = []

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empthy!")
        return
    for student in students:
        student_name = student["name"]
        if student_name.lower() == name.lower():
            print("Name already exist")
            return

    try:
        score = int(input("Enter student score: "))
    except ValueError:
        print("Please enter only number between 0 and 140")
        return
    if score > 140 or score < 0:
        print("Please enter only number between 0 and 140")
        return

    student = {"name": name, "score": score}
    students.append(student)

    with open("students.json", "w") as file:
        json.dump(students, file, indent = 4)

    print("Student added Successfully!")

# Load students from json
def student_load():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            return students
    except json.JSONDecodeError:
        print("List is not available, first add some details.")

# Display all students 2
def student_display():
    students = student_load()
    
    if not students:
        print("Please first add some details.")
        return

    for student in students:
        print("students name:", student["name"], "Score:", student["score"])

# Search students from list 3
def student_search():
    found = False
    students = student_load()

    if not students:
        print("Please first add some details.")
        return
    
    student_search_name = input("Enter student search name: ").lower()
    for student in students:
        student_name = student["name"]         
        if student_name.lower() == student_search_name:
            found = True
            print("Name:", student["name"])
            print("Score:", student["score"])
            break

    if not found:
        print("Not found")

# Students statistics 4
def student_statped():
    students = student_load()

    if not students:
        print("Please first add some details.")
        return

    # Lengh
    print("Number of students:", len(students))
    # Avarage
    S = 0
    for student in students:
        S += int(student["score"])
    print("Average score:", S/(len(students)))
    # Hieghst score
    if not students:
        print("Students not available.")
        return
    max_point = students[0]
    for student in students:
        if max_point["score"] < student["score"]:
            max_point = student
    print("Highest score:", max_point["score"])
    # Top student
    if not students:
        print("No students available.")
        return
    top_student = students[0]
    for student in students:
        if top_student["score"] < student["score"]:
            top_student = student
    print("Top student:", top_student["name"])

print("==========================")
print("STUDENT GRADE MANAGER")
print("==========================")
print("Welcome to Student Grade Manager!")
print("1. Add a student")
print("2. Display all students")
print("3. Search for a student")
print("4. Show grade statistics")
print("5. Exit")

choice = input("Enter your choice: ").strip()
if not choice:
        print("Please enter between 1 and 5!")
        exit()
students = []

if choice == "1":
    student_save()

elif choice == "2":
    student_display()

elif choice == "3":
    student_search()

elif choice == "4":
    student_statped()

elif choice == "5":
    print("Goodbye!")

else:
    print("Invalid syntax")
    print("Please enter between 1 and 5.")