def say_hi(name: str, age: int):
    return f"Hi. My name is {name} and I'm {age} years old."

name = input("Enter name: ")
age = int(input("Enter age: "))

print(say_hi(name, age))
