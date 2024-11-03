# # "a-c" -> abc
# # "a-a" -> a
# # "s-H" -> stuvwxyzABCDEFGH
# # "a-A" -> abcdefghijklmnopqrstuvwxyzA
#
# import string
#
# ALL_LETTERS = string.ascii_letters
# SEPARATOR = "-"
#
# user_input = input("Enter letters in format: 'a-c' ").strip()
#
# if len(user_input) == 3:
#     first_letter = user_input[0]
#     second_letter = user_input[2]
#     separator = user_input[1]
#
#     if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
#         start_index = ALL_LETTERS.index(first_letter)
#         end_index = ALL_LETTERS.index(second_letter)
#
#         if start_index > end_index:
#             start_index, end_index = end_index, start_index
#
#         result = ALL_LETTERS[start_index:end_index + 1]
#         print(result)

##########
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
#            Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

# v1
# number = int(input("Enter your number:"))
# # 123
# while number > 9:
#     result = 1
#     while number > 0:
#         num = number % 10
#         number = number // 10
#         result = result * num
#     number = result
#     print(result)

# v2
# number = int(input("Enter your number:"))
#
# while number > 9:
#     temp_number = str(number)  # 123 -> "123"
#     number = 1
#     for char in temp_number:
#         if char.isdigit():
#             number *= int(char)
#
#     print(number)

###########
# # # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# # Дублікати значень буде видалено.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
#     users.remove(user)  # якщо немає значення – генерується виняток
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
# print(users)
# # #
# users.clear()
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)

# copy() копіювання працює так само як і в list, dict і тд

# users = {"Tom", "Bob", "Alice"}
# users_copy = users.copy()
# users_copy.add("test")
# print(users_copy)
# print(users)

# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# # v2
# print(users & users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
# print(users3)  # {"Tom", "Alice"}
# # v2
# print(users - users2)
# #
# users.difference_update(users2)
# print(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
# print(users3)
#
# # v2
# users4 = users ^ users2
#
# ##
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers))  # True
# print(superusers.issubset(users))  # False
#
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers))  # False
# print(superusers.issuperset(users))  # True
#
# #
# # # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)
# users = set(users)
# print(users)
# # # можна використовувати всі функції звичайного set, крім тих, що модифікують значення

##################################
# функции

##############################
######
# def say_hello():
#     print("Hello")
#
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()  # виклик функції (функція починає працювати)
# say_hello()
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)
# username = "Petya"
# say_hello(username)

#
#
# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
#

# def show_user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# user_hobby = input("Enter your hobby: ")
# show_user_info(name, age, user_hobby)
#
# show_user_info("Petya", 123, user_hobby)

#######################
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)

# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# def add(n1, n2):
#     return n1 + n2
#
#
# def sub(n1, n2): return n1 - n2
#
#
# def mult(n1, n2): return n1 * n2
#
#
# def division(n1, n2): return n1 / n2
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             if second_number == 0:
#                 print("Cannot divide by zero")
#             else:
#                 print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             print("Invalid math operation!")
#
#
# calculate()

# result = add(1, 3)
# print(result)

######

# def say_hi(name, age):
#   return f"Hi. My name is {name} and I'm {age} years old"
#
#
# print(say_hi("Alex", 32))
# print(say_hi("Frank", 68))
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

###########

# def user_info(name: str, age: int = 18, hobby: str = "no hobby"):
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#     if name == "Vasya":
#         return 30
#     if name == "Petya":
#         return 40


# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")

#
# result = user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
# print_person(name="Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)
#
#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

##############
import random
import string


def generate_password(current_pass_len: int, min_password_len: int = 8, max_password_len: int = 16):
    # add pass len validation
    current_pass = ""  # change to list
    for _ in range(current_pass_len):
        # string.ascii_letters + string.digits + string.punctuation move to constant
        current_pass += random.choice(string.ascii_letters + string.digits + string.punctuation)

    return current_pass


my_pass = generate_password(10)
print(my_pass)

