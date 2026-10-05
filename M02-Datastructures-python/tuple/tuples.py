# Index
names = ("Alice", "Bob", "Charlie", "Bob")
print(names, type(names), len(names))
print(names.count("Bob"))
print(names.index("Bob"))
print(names[3])
print(names[-2])
yn = names[0:3]
print(yn, type(yn))

# Loop
for n in names:
    print(n)

fruits = ("apple",)
print(fruits, type(fruits))
print(fruits * 3, type(fruits))

# Constructor
stu_info = tuple(["Alice", 15, 23000, True])
print(stu_info, type(stu_info))

n = 10
print(n, type(n))
numbers = 1, 2, 3, 4, 5
print(numbers, type(numbers))
#numbers[1] = 200 # Immutable
del numbers
# print(numbers)

age = [10, 20]
age[1] = 25
print(age)

# Tuple Packing and Unpacking
# unpacking
fruits = ("apple", "banana", "cherry")
(f1, *f2) = fruits
print(f1)
print(f2, type(f2))

# packing
a = 10
b = 20
c = 30
numbers = (a, b, c)
print(numbers, type(numbers))

a = (1, 2, 3)
b = (5, 6, 7, 8)
# print(a, extend(b))
c = a + b
print(c, type(c))