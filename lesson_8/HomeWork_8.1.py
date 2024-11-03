def add_one(digits):

    number = int(''.join(map(str, digits)))

    number += 1

    return [int(digit) for digit in str(number)]


result = add_one([9, 9, 9])
print(result)
