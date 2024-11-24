class GroupFullError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupFullError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"


# Додаткові класи (для збереження сумісності)
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 28, 'Anna', 'Smith', 'AN147')
st5 = Student('Male', 20, 'Mark', 'Lee', 'AN148')
st6 = Student('Female', 23, 'Lucy', 'Brown', 'AN149')
st7 = Student('Male', 24, 'James', 'White', 'AN150')
st8 = Student('Female', 21, 'Clara', 'Green', 'AN151')
st9 = Student('Male', 29, 'Tom', 'Harris', 'AN152')
st10 = Student('Female', 26, 'Sophia', 'Adams', 'AN153')
st11 = Student('Male', 25, 'Peter', 'Parker', 'AN154')

gr = Group('PD1')

try:
    for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]:
        gr.add_student(student)
except GroupFullError as e:
    print(e)  # У групі не може бути більше 10 студентів

print(gr)
