# def hello(): print("Hello")
#
#
# print(hello)
# message = hello  # надав посилання на функцію в іншу змінну
# print(message)
#
# hello()
# message()

##################
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid operation!")


# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 0)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

# button=lambda: print("Hello world!")

# def test(a, b):
#     return 2

# button=lambda: test(1, 3)

#####
# message = lambda: print("Hello world!")
# message()
# print(message)
# print(lambda: print("Hello world!"))


####
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))


# def calculate(a, b, math_operation) -> None:
#     print(math_operation)
#     print(f"Result: {math_operation(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)

###
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b  # повернення посилання на функцію
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

####
# LEGB - почитати
# https://www.bestprog.net/uk/2020/07/29/python-the-scopes-of-names-in-python-local-names-visibility-rules-for-names-legb-rule-the-global-keyword-overriding-names-in-functions-ua/

#####
# області видимості
# number = 10
#
#
# def test():
#     # number = 11  # перекриття глобальної змінної
#
#     if 1:
#         # number = 12
#
#         if 1:
#             # number = 13
#             num = 20
#             print(number)
#     print(number)
#     # print(num)


# print(number)
# test()
# print(number)
# number = 35
# print(number)

##########
# number = 10
#
#
# def test():
#     global number
#
#     number = 11  # змінюємо значення глобальної змінної
#     print(number)
#
#
# print(number)
# test()
# print(number)

#########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

#############
###

# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = 10
#
#     def inner():
#         global number
#         nonlocal new_number
#         new_number = 2
#         print(new_number)
#         my_test = 111
#         number = 2
#
#         def inner_number_2():
#             global number
#             nonlocal new_number
#             nonlocal my_test
#             new_number = 3
#             print(new_number)
#             print(my_test)
#             number = 3
#
#         inner_number_2()
#
#     def test():
#         nonlocal new_number
#         new_number = 333
#         # nonlocal my_test
#         # print(my_test)
#         print(new_number)
#
#     inner()
#     test()
#     print(new_number)
#
#
# outer()
# print(number)


# import math
#
#
# #####
# def get_list_with_min_avg(input_data):
#     def get_avg(input_list):
#         return sum(input_list) / len(input_list)
#
#     min_avg = math.inf
#     current_min_avg_list = []
#
#     for nums_list in input_data:
#         current_avg = get_avg(nums_list)
#         if min_avg > current_avg:
#             min_avg = current_avg
#             current_min_avg_list = nums_list
#
#     return min_avg, current_min_avg_list
#
#
# data = [
#     [1, 2],
#     [3, 1],
#     [0, 4]
# ]
# result = get_list_with_min_avg(data)
# print(result)

###########
# def show_info(number, *args, text="no text"):
#     print(number)
#     print(args)
#     print(text)
#
#
# show_info(10, 2, 3, 4, 5, 6, 7, 8, 9, text="hello")
#
#
# def show_info(num, *args, data="test", **kwargs):
#     print(num)
#     print(args)
#     print(data)
#     print(kwargs)
#
#
# show_info(100, 2, "hello", 1234, 3456, data="my data", number=10, text="hello")


# def my_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# my_func(1, 2, "test", 5, name="John", age=23)

# ####
# def show_info(name, age, hobby):
#     print(f'Name: {name}, Age: {age}, Hobby: {hobby}')


# user_data = ["Vasya", 123, "Test"]
# # v1
# show_info(user_data[0], user_data[1], user_data[2])
# # v2 (распаковка)
# show_info(*user_data)
#
# user_data = {
#     "name": "Petya",
#     "age": 33,
#     "hobby": "My hobby"
# }
#
# # v1
# show_info(user_data.get("name"), user_data.get("age"), user_data.get("hobby"))
# # v2 (распаковка)
# show_info(**user_data)

##############
# 1. Створити список чисел.
# - Заберіть дублікати значень.
# - Вивести унікальні значення.

# import random
#
#
# def create_list_with_random_numbers(list_length=10, start_value=1, end_value=5) -> list[int]:
#     return [random.randint(start_value, end_value) for _ in range(list_length)]
#
#
# def remove_duplicates(input_list: list[int]) -> list[int]:
#     return list(set(input_list))
#
#
# def get_unique_values(input_list: list[int]) -> list[int]:
#     return [number for number in input_list if input_list.count(number) == 1]
#
#
# numbers_list = create_list_with_random_numbers()
# print(numbers_list)
# numbers_list_without_duplicates = remove_duplicates(numbers_list)
# print(numbers_list_without_duplicates)
# numbers_list_unique_values_only = get_unique_values(numbers_list)
# print(numbers_list_unique_values_only)


# import math
#
#
# def calculate_circle_area(radius):
#     if radius < 0:
#         return print("Radius can't be a negative number")
#
#     area = math.pi * (radius ** 2)
#     return area
#
#
# print(calculate_circle_area(int(input("Enter radius: "))))

# def sum_of_digits(number):
#     number = abs(number)
#     total = 0
#
#     for digit in str(number):
#         total += int(digit)
#     number = total
#
#     return number
#
#
# input_number = -9876
# result = sum_of_digits(input_number)
# print("Result: ", result)


# def reverse_words(sentence):
#
#     words = sentence.split()
#
#     reversed_words = [word[::-1] for word in words]
#
#     return ' '.join(reversed_words)
#
#
# input_sentence = "Python is fun"
# result = reverse_words(input_sentence)
# print("Result:", result)

