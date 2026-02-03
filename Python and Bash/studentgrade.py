student={}
# while True:
#     name=input("Enter student name (or 'exit' to finish): ")
#     if name.lower()=='exit':
#         break
#     grade=input(f"Enter grade for {name}: ")
#     student[name]=grade
# for name, grade in student.items():
#     print(f"{name}: {grade}")
while True:
    print("\n1. Add Student and grade")
    print("2. Update Student grade")
    print("3. View Students")
    print("4. Exit")
    choice=input("Enter your choice (1-4): ")
    if choice=='1':
        name=input("Enter student name: ")
        grade=input(f"Enter grade for {name}: ")
        student[name]=grade
        print(f"Added {name} with grade {grade}.")
    elif choice=='2':
        name=input("Enter student name to update: ")
        if name in student:
            grade=input(f"Enter new grade for {name}: ")
            student[name]=grade
            print(f"Updated {name} to grade {grade}.")
        else:
            print(f"Student {name} not found.")
    elif choice=='3':
        if student:
            print("Student Grades:")
            for name, grade in student.items():
                print(f"{name}: {grade}")
        else:
            print("No students found.")
    elif choice=='4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")