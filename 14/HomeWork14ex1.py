# ДЗ 14.1. Виняток користувача
class TooManyStudents(Exception):
    def __init__(self, msg="Maximum number of students is 10"):
        super().__init__(msg)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'{self.first_name} {self.last_name}, '
                f'age {self.age} gender {self.gender}')


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student {super().__str__()} with book {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudents()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '


gr = Group('PD1')

try:
    # додаємо 10 студентів
    for i in range(12):
        gr.add_student(Student('Male', 20+i, f'Name{i}',
                               f'Last{i}', f'RB{i}'))
    print("10 студентів додано успішно")
except TooManyStudents as e:
    print("Помилка:", e)
