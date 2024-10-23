CONTINUE_PROGRAM_USER_SELECT = "y"
while True:
    number_1 = int(input('Введіть перше число: '))
    number_2 = int(input('Введіть друге число: '))
    action = input('Оберіть бажану операцию (+, -, /, *): ')

    if action == '+':
        result = number_1 + number_2
        print(f'Результат: {number_1} + {number_2} = {result}')

    elif action == '-':
        result = number_1 - number_2
        print(f'Результат: {number_1} - {number_2} = {result}')

    elif action == '/':
        if number_2 == 0:
            print('Ділення на нуль не можливе!')

        else:
            result = divmod(number_1, number_2)
            print(f'Результат: {number_1} / {number_2} = {f'{result[0]},{result[1]}'}')

    elif action == '*':
        result = number_1 * number_2
        print(f'Результат: {number_1} * {number_2} = {result}')

    else:
        print('Не вірно обрана операція')

    is_continue = input(f"Бажаєте продовжити? \'{CONTINUE_PROGRAM_USER_SELECT}\' для продовження: ")

    if is_continue != CONTINUE_PROGRAM_USER_SELECT:
        print("Вихід з програми...")
        break