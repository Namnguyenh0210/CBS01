#Ứng dụng các nguyên lý của lập trình hướng đối tượng, hãy viết chương trình quản lý điểm của học viên. Chương trình có các chức năng như thêm học viên mới, thêm điểm số của học viên, tính điểm trung bình và lưu điểm vào file
#Tạo menu tương tác với người dùng như sau: 
# 1.	Add a new student 
# 2.	Record a grade for a student 
# 3.	Calculate the average grade of all students 
# 4.	Save the data to a file 
# 5.	Exit 
# Enter your choice (1-5): 

# Tạo lớp Student với các thuộc tính sau:
#  ● name: Tên học viên 
# ●	grades: Danh sách điểm của học viên và các phương thức sau: 
# ●	__init__ 
# ●	add_grade(grade): Thêm điểm mới vào danh sách điểm 
# ●	calculate_average: Tính điểm trung bình của học viên 
 
# Tạo lớp GradeManager với các thuộc tính sau: 
# ●	students: Danh sách các học viên và các phương thức sau: 
# ●	__init__ 
# ●	add_student(name): Thêm học viên mới vào danh sách 
# ●	record_grade(name, grade): Tìm tên học viên và thêm điểm mới vào danh sách điểm của học viên đó 
# ●	calculate_average_all: Tính điểm trung bình của toàn thể học sinh 
# ●	save_data(filename): Lưu điểm trung bình của học sinh vào file 

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)

    def record_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                break

    def calculate_average_all(self):
        total = 0
        for student in self.students:
            total += student.calculate_average()
        return total / len(self.students)

    # def save_data(self, filename):
    #     with open(filename, 'wb') as file:
    #         pickle.dump(self.students, file)

if __name__ == '__main__':
    grade_manager = GradeManager()

    while True:
        print('Menu:')
        print('-------------------------')
        print('1. Add a new student')
        print('2. Record a grade for a student')
        print('3. Calculate the average grade of all students')
        prin
        print('6. Exit')
        choice = input('Enter your choice (1-5): ')
        print('-------------------------')

        if choice == '1':
            name = input('Enter the name of the student: ')
            grade_manager.add_student(name)
        elif choice == '2':
            name = input('Enter the name of the student: ')
            grade = float(input('Enter the grade: '))
            grade_manager.record_grade(name, grade)
        elif choice == '3':
            print('The average grade of all students is:', grade_manager.calculate_average_all())
        elif choice == '4':
            filename = input('Enter the filename: ')
            grade_manager.save_data(filename)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

    grade_manager.load_data('data.pkl')

    print('The average grade of all students is:', grade_manager.calculate_average_all())
    print('Data loaded from file')
    print('Students:')
    for student in grade_manager.students:
        print(student.name, ':', student.calculate_average())
        print('Grades:', student.grades)

    input('Press Enter to exit...')

