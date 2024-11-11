####
# Рекурсія – коли функція викликає сама себе
# 1. продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. визначити умову або умови виходу з рекурсії
# 3. запустити рекурсію (виклик цієї ж функції)

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)
#
#
# print(factorial(5))
#
#
# factorial(5) -> 5 * factorial(4) => 120
# factorial(4) -> 4 * factorial(3) => 24
# factorial(3) -> 3 * factorial(2) => 6
# factorial(2) -> 2 * factorial(1) => 2
# factorial(1) => 1

# Написати рекурсивну функцію знаходження ступеня числа.
# def my_pow(base, exponent):
#     if exponent <= 1:
#         return base
#
#     return base * my_pow(base, exponent-1)
#
#
# result = my_pow(2, 3)
# print(result)

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

###
# f(n) = f(n-1) + f(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number - 1) + fib(number - 2)
#
#
# # print(fib(4))
#
# for i in range(10):
#     print(fib(i), end=" ")

##############
# # Приклад: Зіпувати два списки
# names = ['Alice', 'Bob', 'Charlie', 'David']
# ages = [25, 30, 22, 55]
# zipped_data = zip(names, ages)
# result = list(zipped_data)
# print(result)
# Вивід: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]


# # Приклад: Застосувати функцію до парних чисел
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
# final_result = list(result)
# print(final_result)  # Вивід: [4, 16, 36, 64, 100]


# Приклад: Застосування квадратного кореня до кожного елемента списку
# def my_sqrl(number):
#     return number**0.5
#
#
# numbers = [1, 2, 3, 4, 5]
# # squared_root = map(lambda x: x**0.5, numbers)
# squared_root = map(my_sqrl, numbers)
# result = list(squared_root)
# print(result)  # Вивід: [1.0, 1.414, 1.732, 2.0, 2.236]

####
# Генератори колекцій
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: джерело даних, що перебирається, в якості якого може виступати список, безліч, послідовність,
# або навіть функція, яка повертає набір даних, наприклад, range()
#
# item: елемент, що витягується з джерела даних
#
# expression: вираз, який повертає певне значення. Це значення потім потрапляє в список, що генерується
#
# condition: умова, якій повинні відповідати елементи, що витягуються з джерела даних.
# Якщо елемент НЕ задовольняє умову, він не вибирається. Необов'язковий параметр.

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
# #
# # # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)
#
# #
# nums = [n for n in range(10)]
# print(nums)
#
# #
# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)
#
# #
# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)
#
# #
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)
#
# # #
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# #
# my_set = {i for i in range(10)}
# print(my_set)

#################
# import random
# # # from random import *
# # from random import randint, choice
#
#
# print(random.randint(1, 100)) # від 1 до 100
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(10)) # від нуля до 9
# print(random.randrange(2, 10)) # від 2 до 9
# print(random.randrange(2, 10, 2)) # від 2 до 9 через один (кожен другий)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums) # перемішуємо значення списку
# print(nums)

###
# import math
#
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))  # 2 ** 3
# print(math.sqrt(9))

##
# from decimal import *
#
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.0000"))
# print(number)
#
# number = Decimal("12.123456789")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.5555")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.9999")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# # округлення відбувається до найближчого парного числа, якщо округлена частина дорівнює 5
# number = Decimal("12.025")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.035")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

###
# datetime
# import datetime as dt
#
# print(dt.date.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
# # #
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
# #
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# https://www.programiz.com/python-programming/datetime/strftime
#
# from datetime import datetime, timezone, timedelta
#
# # naive
# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# # UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# # Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)
#
# # https://pynative.com/python-timezone/

##################
# \d - відповідає будь-якій одній цифрі і замінює собою вираз [0-9];
# \D - виключає всі цифри та замінює [^0-9];
# \w - Замінює будь-яку цифру, букву, а також знак нижнього підкреслення;
# \W - будь-який символ крім латиниці, цифр або нижнього підкреслення;
# \s - відповідає будь-якому пробельного символу;
# \S - описує будь-який непробільний символ.
#
#
# . Один символ, крім нового рядка \n.
# ? 0 або 1 входження шаблону зліва
# + 1 і більше входжень шаблону зліва
# * 0 і більше входжень шаблону зліва
# \w Будь-яка цифра або буква (\W - все, крім букви або цифри)
# \d Будь-яка цифра [0-9] (\D - все, крім цифри)
# \s Будь-який символ пробілу (\S - будь-який символ пробілу)
# \b Кордон слова
# [..] Один із символів у дужках ([^..] — будь-який символ, крім тих, що у дужках)
# \ Екранування спеціальних символів (\. означає точку або \+ - знак "плюс")
# ^ і $ Початок і кінець рядка відповідно
# {n,m} Від n до m входжень ({,m} - від 0 до m)
# a|b Відповідає a або b
# () Групує вираз і повертає знайдений текст
# \t, \n, \r Символ табуляції, нового рядка та повернення каретки відповідно
#
# Для чого використовуються регулярні вирази
# для визначення потрібного формату, наприклад, телефонного номера або email-адреси;
# для розбивки рядків на підрядки;
# для пошуку, заміни та вилучення символів;
# для швидкого виконання нетривіальних операцій.
#
# А ось найбільш популярні методи, які надає модуль:
#
# re.match() - Цей метод шукає за заданим шаблоном на початку рядка
# re.search() - Метод схожий на match(), але шукає не лише на початку рядка
# re.findall() - Повертає список усіх знайдених збігів.
# У методу findall() немає обмежень на пошук на початку або в кінці рядка.
# re.split() - Цей метод поділяє рядок за заданим шаблоном
# re.sub() - Шукає шаблон у рядку і замінює його на вказаний підрядок.
# Якщо шаблон не знайдено, рядок залишається незмінним
# re.compile() - Ми можемо зібрати регулярне вираження в окремий об'єкт, який можна використовувати для пошуку.
# Це також позбавляє переписування одного і того ж виразу.

import re

# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))
# #
# #
# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())
# #
# #
# result = re.findall(r'he', 'hello world hello')
# print(result)
# #
# #
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
# #
# result = re.split(r'l', 'hello world hello')
# print(result)  # ['he', '', 'o wor', 'd he', '', 'o']
# #
# #
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)

# result = re.findall(r'.', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w*', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+$', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'^\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\b\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
# print(result)
#
# result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
# print(result)
#
# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
# print(result)

# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
#
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# додатково:
#
# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ,
# довжина пароля – від 8 до 16 символів)



# # """
# # Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# # - домашній номер телефону (тільки цифри та довжина номера)
# # - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# # - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# # - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# # додатково:
# # - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра,
# # один символ, довжина пароля – від 8 до 16 символів)
# # """
# #
# import re
# import random
# import string
#
# MIN_SIZE_PASSWORD = 8
# MAX_SIZE_PASSWORD = 16
#
#
# def generate_password(length: int = MIN_SIZE_PASSWORD) -> str:
#     """
#     Генерує пароль, який відповідає наступним вимогам:
#     - мінімум одна велика літера
#     - мінімум одна маленька літера
#     - мінімум одна цифра
#     - мінімум один символ
#     - загальна довжина пароля - від 8 до 16 символів (за замовчуванням 8)
#     """
#     if not (MIN_SIZE_PASSWORD <= length <= MAX_SIZE_PASSWORD):
#         print(f"Довжина пароля повинна бути від {MIN_SIZE_PASSWORD} до {MAX_SIZE_PASSWORD} символів")
#         return
#         # raise ValueError(f"Довжина пароля повинна бути від {MIN_SIZE_PASSWORD} до {MAX_SIZE_PASSWORD} символів")
#
#     # Визначаємо набори символів
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     digits = string.digits
#     symbols = "@$!%*?&"
#
#     # Гарантуємо наявність хоча б одного символу з кожного набору
#     password = [
#         random.choice(lower),
#         random.choice(upper),
#         random.choice(digits),
#         random.choice(symbols)
#     ]
#
#     # Додаємо випадкові символи для досягнення бажаної довжини пароля
#     all_chars = lower + upper + digits + symbols
#     password += [random.choice(all_chars) for _ in range(length - 4)]
#
#     # Перемішуємо символи, щоб уникнути передбачуваності
#     random.shuffle(password)
#
#     # Повертаємо пароль як рядок
#     return ''.join(password)
#
#
# def validation(pattern: str, expression: str) -> bool:
#     return bool(re.match(pattern, expression))
#     # Повертає True, якщо вираз відповідає шаблону, інакше - False
#
#
# 1.
# expression = ""
# pattern = r"^\d{5,7}$"
# print("1. Home phone number can be from 5 to 7 digits long.")
# while not validation(pattern, expression):
#     expression = input("Enter your home phone number to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Number {expression} is valid. It looks like your home phone.")
# print()
#
# # 2.
# pattern = r"^\+?\d{1,3}\s?\d{1,5}\s?\d{5,8}$"
# # """
# # Код країни в міжнародних номерах зазвичай складається з 1 до 3 цифр. Довжина коду країни залежить від конкретної
# # країни і може змінюватись.
# # Код оператора мобільного зв'язку або міста у телефонних номерах може складатися з різної кількості цифр, залежно
# # від країни та конкретної телефонної системи. Загалом, для мобільних операторів та міських телефонних систем кількість
# # цифр у коді може змінюватись від 1 до 5.
# # Локальний номер телефону без урахування коду країни та коду оператора або міста зазвичай складається з 5 до 8 цифр,
# # залежно від країни та конкретної телефонної системи.
# # """
# print("2. Mobile phone number can be from 10 to 12 digits long and may optionally contain + at the beginning"
#       " or spaces after the country code and operator code.")
# expression = ""
# while not validation(pattern, expression):
#     expression = input("Enter your mobile phone number to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Number {expression} is valid. It looks like your mobile phone.")
# print()
#
# # 3.
# expression = ""
# pattern = r"^[a-zA-Z0-9]+[._]?[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-Z]{2,}$"
# # # ^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# # # Цей патерн розбивається на такі частини:
# # # ^[a-zA-Z0-9._%+-]+ - початок рядка повинен містити один або більше символів, які можуть бути літерами (a-z, A-Z),
# # # цифрами (0-9), точками (.), підкресленнями ( _), відсотками (%), плюсами (+) чи мінусами (-).
# # # @ - символ собаки, що розділяє ім'я користувача та домен поштового сервісу.
# # # [a-zA-Z0-9.-]+ - доменне ім'я, що складається з літер, цифр, точок або дефісів.
# # # \. - точка, що відокремлює доменне ім'я від доменного суфікса.
# # # """[a-zA-Z]{2,} - доменний суфікс, що складається з двох або більше букв (наприклад, "com", "org", "net").
# # # Це базовий патерн і він підходить для більшості звичайних адрес електронної пошти, проте варто зауважити, що існують
# # # специфічні випадки адрес, які можуть не задовольняти цей вираз через особливі символи або нові доменні зони.
# print("3. Example for e-mail address : press@google.com")
# while not validation(pattern, expression):
#     expression = input("Enter your e-mail adress to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Expression {expression} is valid. It looks like e-mail adress.")
# print()
#
# # 4.
# expression = ""
# pattern = r"^([A-Za-zА-Яа-яҐЄІЇґєії]{2,20}\s){2}[A-Za-zА-Яа-яҐЄІЇґєії]{2,20}$"
# print("4. Last name, first name and patronymic of the client (3 words, minimum 2 char, maximum 20 char).")
# while not validation(pattern, expression):
#     expression = input("Enter last name, first name and patronymic of the client to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(
#             f"Validation OK. Expression {expression} is valid. It looks like last name, first name and patronymic of the client.")
# print()
#
# # 5.
# expression = ""
# pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
# # Розшифровка компонентів цього виразу:
# # ^ і $ - позначають початок і кінець рядка відповідно, що гарантує перевірку всього рядка.
# # (?=.*[a-z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї маленької літери.
# # (?=.*[A-Z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї великої літери.
# # (?=.*\d) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї цифри.
# # (?=.*[@$!%*?&]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б одного символу з вказаного набору.
# # [A-Za-z\d@$!%*?&]{8,16} - вказує на те, що дозволені літери (великі та маленькі), цифри та символи з вказаного набору,
# # а довжина рядка має бути від 8 до 16 символів.
# # Цей регулярний вираз гарантує, що пароль буде відповідати всім вказаним вимогам: міститиме велику та маленьку літери,
# # цифру, спеціальний символ і матиме довжину від 8 до 16 символів.
# print(f"5. Password (minimum: one capital letter, one small letter, one number, one symbol, password length -"
#       f" from {MIN_SIZE_PASSWORD} to {MAX_SIZE_PASSWORD} characters). Example for password:"
#       f" {generate_password()}")
# while not validation(pattern, expression):
#     expression = input("Enter your home password to verify: ")
#     if MIN_SIZE_PASSWORD <= len(expression) <= MAX_SIZE_PASSWORD:
#         if not validation(pattern, expression):
#             print("Validation Error. Please try again.")
#         else:
#             print(f"Validation OK. Expression {expression} is valid. It looks like your password.")
#     else:
#         print("Validation Error. Please try again.")
# print()

