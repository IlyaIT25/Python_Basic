# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

# numbers = [6]
#
# if len(numbers) != 0:
#     my_sum = 0
#
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             my_sum += numbers[i]
#
#     result = my_sum * numbers[-1]
# else:
#     result = 0
#
# print(f"Result: {result}")

####
###
# message = "hello world"
# [] -> індексатори
# Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])
#
# ###
# # # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# # slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)

#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(65))
# print(chr(99))
#
# ####
# text = "helLo woRlD"
#
# # isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
#
# # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
#
# print(text.capitalize())
# #
# fio = input("Enter fio: ").title()
# print(fio)
#
#
# lstrip(): видаляє початкові пробіли з рядка
# text = "        helLo woRlD         "
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())

# # ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width,
# # то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
# text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
# #
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
# #
# print(text.find("p"))  # -1
# #
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

# # replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)

###############
# text = "hello world. goodbye world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentence = search_item.join(result)
# print(result_sentence)

##########
import keyword
print(keyword.kwlist)

import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.digits)

#################
# import random
# import string
#
# MIN_PASSWORD_LENGTH = 8
# MAX_PASSWORD_LENGTH = 20
# CONTINUE_PROGRAM_USER_SELECT = "y"
# DATA_FOR_PASSWORD = string.ascii_letters + string.digits + string.punctuation
#
# while True:
#     password = []
#
#     password_length = input(f"Enter password length from {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}: ")
#
#     if password_length.isnumeric():
#         password_length = int(password_length)
#
#         if password_length > MAX_PASSWORD_LENGTH or password_length < MIN_PASSWORD_LENGTH:
#             print("Incorrect password length")
#             continue
#
#         for _ in range(password_length):
#             password.append(random.choice(DATA_FOR_PASSWORD))
#
#         random.shuffle(password)
#         new_password = "".join(password)
#         print(f"Your password is: {new_password}")
#     else:
#         print("Password length should be numeric")
#
#     is_continue = input(f"Do you want to continue? \'{CONTINUE_PROGRAM_USER_SELECT}\' for yes: ")
#
#     if is_continue != CONTINUE_PROGRAM_USER_SELECT:
#         print("Exit from program...")
#         break

###################################
# numbers = [1, 2, [1, 4], 5, [6, 9]]
# print(numbers)
# print(numbers[1])
# print(numbers[-1])
# print(numbers[-1][0])

# matrix = [
#     [1, 3, 5],
#     [2, 4],
#     [6, 2, 8]
# ]
#
# print(matrix)
# print(matrix[2][1])

###################################
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
#
# вивести на екран
#
# - вивести суму чисел головної діагоналі матриці
#
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
#
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
#
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

#################################
# import random
#
# matrix = []
#
# # print(matrix)
# for i in range(5):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(random.randint(10, 99))
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()
#
# # - вивести суму чисел головної діагоналі матриці
#
# general_diagonal_sum = 0
# counter = 1
#
# for row in matrix:
#     general_diagonal_sum += row[len(row) - counter]
#     # print(row[len(row) - counter])
#     counter += 1
#
# print(f"General diagonal sum: {general_diagonal_sum}")

# - вивести мінімальне та максимальне значення побічної діагоналі матриці

# numbers = []
#
# for i in range(len(matrix)):
#     numbers.append(matrix[i][i])
#
# print(f"Min value: {min(numbers)}")
# print(f"Max value: {max(numbers)}")

# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)

# ROWS = 5
#
# direction = int(input("Enter direction:\n1. Vertical\n2. Horizontal: "))
#
# match direction:
#     case 1:
#         number = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         if 1 <= number <= len(matrix):
#             for i in range(len(matrix)):
#                 print(matrix[i][number - 1], end=" ")
#         else:
#             print("column number out of range!")
#     case 2:
#         number = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         if 1 <= number <= len(matrix):
#             for num in matrix[number - 1]:
#                 print(num, end=" ")
#         else:
#             print("row number out of range!")
#     case _:
#         print("Incorrect matrix direction!")

# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

# ROWS = 5
#
# direction = int(input("Enter direction:\n1. Vertical\n2. Horizontal: "))
#
# match direction:
#     case 1:
#         first_column = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         second_column = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         if 1 <= first_column <= len(matrix) and 1 <= second_column <= len(matrix) and first_column != second_column:
#             for i in range(len(matrix)):
#                 matrix[i][first_column - 1], matrix[i][second_column - 1] =\
#                     matrix[i][second_column - 1], matrix[i][first_column - 1]
#
#             for row in matrix:
#                 for number in row:
#                     print(number, end=" ")
#                 print()
#         else:
#             print("Incorrect column number!")
#     case 2:
#         first_row = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         second_row = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         if 1 <= first_row <= len(matrix) and 1 <= second_row <= len(matrix) and first_row != second_row:
#             matrix[first_row - 1], matrix[second_row - 1] = matrix[second_row - 1], matrix[first_row - 1]
#
#             for row in matrix:
#                 for number in row:
#                     print(number, end=" ")
#                 print()
#         else:
#             print("Incorrect column number!")
#     case _:
#         print("Incorrect matrix direction!")

##########################
