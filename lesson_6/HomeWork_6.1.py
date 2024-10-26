# V1

# import string

# input_text = input("Enter range: ")
#
# first_letter, second_letter = input_text.split("-")
#
# if string.ascii_letters.index(first_letter) < string.ascii_letters.index(second_letter):
#     print(string.ascii_letters[string.ascii_letters.index(first_letter):string.ascii_letters.index(second_letter) + 1])
#
# else:
#     print(string.ascii_letters[string.ascii_letters.index(second_letter):string.ascii_letters.index(first_letter) + 1])


# V2

import string

input_text = input("Enter range: ")

first_letter, second_letter = input_text.split("-")

first_index = string.ascii_letters.index(first_letter)  # находим индексы символов из конст
second_index = string.ascii_letters.index(second_letter)

if first_index < second_index:
    print(string.ascii_letters[first_index:second_index + 1])

else:
    print(string.ascii_letters[second_index:first_index + 1])