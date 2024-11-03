def find_unique_value(numbers):
    for number in numbers:

        if numbers.count(number) == 1:
            return number

    return None

print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
