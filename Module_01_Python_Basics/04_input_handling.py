# 04 - Input Handling in Python
# ------------------------------------------------------------

# Static variable output
name = "Mahadev"
print(f"My name is {name}!")

print("-" * 30)

# Dynamic input from user
# Note: input() always returns data of type 'str'
name = input("Enter your name: ")
print(f"My name is {name}")

age = input("Enter your age: ")
print(f"My age is {age}")

print("-" * 30)

# Typecasting input to integer for arithmetic operations
# Add two numbers:
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = a + b
print(f"The sum of {a} and {b} is: {c}")
