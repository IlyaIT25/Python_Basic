numbers = int(input("Enter number: "))

while numbers > 9:
    product = 1
    for digit in str(numbers):
        product *= int(digit)

    numbers = product
print("Result:", numbers)