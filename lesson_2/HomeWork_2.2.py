number = int(input('Enter a number: '))
n1 = number // 10000
n2 = number % 10000 // 1000
n3 = number % 1000 // 100
n4 = number // 10 % 10
n5 = number % 10
print(str(n5) + str(n4) + str(n3) + str(n2) + str(n1))