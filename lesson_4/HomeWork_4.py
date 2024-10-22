#Задание 4.1
#
# numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# for i in range(numbers.count(0)):
#     numbers.remove(0)
#     numbers.append(0)
# print(numbers)


#Задание 4.2
#
# numbers = [0, 1, 7, 2, 4, 8]
# print(sum(numbers[0:6:2]) * (numbers[(len(numbers) - 1)])) # индекс 0 относим к чётным числам

#

# Задание 4.3
#
import random
numbers = []
for i in range(random.randint(3, 10)):
    numbers.append(random.randint(3, 10))
# print(numbers) # для возможности проверить
print(numbers[0],numbers[2],numbers[-2])
