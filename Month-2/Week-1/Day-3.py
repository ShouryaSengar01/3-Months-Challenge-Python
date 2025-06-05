# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     Shared Among all instances of a Class
# ░░      ⭐ CLASS VARIABLES ⭐      ░░  => Defines outside the constructor
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     Allows you to share data among all objects created from that class

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 26)
student2 = Student("Patrick", 32)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)
# print(Student.num_students)
print(f"My graduating class of {Student.class_year} had {Student.num_students} Students")
print(student1.name, student2.name, sep= "\n")
