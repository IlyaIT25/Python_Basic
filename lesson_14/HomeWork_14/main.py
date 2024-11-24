from student import Student
from lesson_14.HomeWork_14.group import Group

# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створення групи
gr = Group('PD1')

# Додавання студентів
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Перевірка пошуку та порівняння
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

# Видалення студента
gr.delete_student('Taylor')
print(gr)  # Тепер у групі тільки один студент
