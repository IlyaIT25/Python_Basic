import keyword
import string
# print(string.punctuation)
# print(keyword.kwlist)

user_name = input("Enter your user name: ")

if not user_name[:1] in string.digits:  # проверка на начало с цифры

    if not any(char in string.ascii_uppercase for char in user_name): # Проверка на большие буквы

        if not user_name in keyword.kwlist:  # Проверка на ключевые слова

            if not any(char in string.punctuation or char == " " for char in user_name if char != "_"): # Проверка на знаки

                if user_name.count('_') <= 1: # Проверка на кол-во _
                    print('True')
                else: print("False")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
else:
    print("False")
