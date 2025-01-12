#Hãy viết một chương trình quản lý điểm số của học viên. Chương trình cần có hai lớp Student và StudentManager
#lớp Student sẽ có 2 thuộc tính là name & grade

#Cần tạo ra một menu options


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} - {self.grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def display_students(self):
        for student in self.students:
            print(student)


student_manager = StudentManager()


# menu options
def menu_options():
    print("-------------------------")
    print("Student Management System")
    print("Choose an option:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Exit")
    print("-------------------------")
   

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            grade = float(input("Enter grade: "))
            student = Student(name, grade)
            student_manager.add_student(student)
        elif choice == 2:
            name = input("Enter name: ")
            student_manager.remove_student(name)
        elif choice == 3:
            student_manager.display_students()
        elif choice == 4:
            break
        else:
            print("vui long chon lai")
 



# run the menu
menu_options()
    



