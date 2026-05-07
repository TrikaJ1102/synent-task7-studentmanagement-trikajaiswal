import json
import os

FILE_NAME = "students.json"


# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View students
def view_students(students):
    if not students:
        print("\nNo student records found.")
    else:
        print("\n===== STUDENT RECORDS =====")

        for index, student in enumerate(students, start=1):
            print(f"""
Student {index}
-------------------
Name   : {student['name']}
Roll   : {student['roll']}
Course : {student['course']}
""")


# Update student
def update_student(students):
    view_students(students)

    if students:
        try:
            student_num = int(input("Enter student number to update: "))

            if 1 <= student_num <= len(students):
                print("\nEnter new details:")

                students[student_num - 1]["name"] = input("New name: ")
                students[student_num - 1]["roll"] = input("New roll number: ")
                students[student_num - 1]["course"] = input("New course: ")

                save_students(students)

                print("Student updated successfully!")

            else:
                print("Invalid student number.")

        except ValueError:
            print("Please enter a valid number.")


# Delete student
def delete_student(students):
    view_students(students)

    if students:
        try:
            student_num = int(input("Enter student number to delete: "))

            if 1 <= student_num <= len(students):
                removed = students.pop(student_num - 1)

                save_students(students)

                print(f"Student '{removed['name']}' deleted successfully!")

            else:
                print("Invalid student number.")

        except ValueError:
            print("Please enter a valid number.")


# Main menu
def main():
    students = load_students()

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print("Exiting Student Management System...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()