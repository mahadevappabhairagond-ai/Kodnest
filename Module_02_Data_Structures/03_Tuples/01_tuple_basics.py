# 01 - Tuple Basics, Operations & Packing in Python
# ------------------------------------------------------------

# 1. Tuple Creation, Length, Count & Indexing
names = ("Alice", "Bob", "Charlie", "Bob")
print("names:", names)
print("type:", type(names))
print("length:", len(names))
print("count('Bob'):", names.count("Bob"))
print("index('Bob'):", names.index("Bob"))
print("names[3]:", names[3])
print("names[-2]:", names[-2])
yn = names[0:3]
print("Slice yn:", yn, "| Type:", type(yn))
print("-" * 40)

# 2. Iterating through a Tuple
print("Iterating through names:")
for n in names:
    print(n)
print("-" * 40)

# 3. Single-element Tuple (Requires trailing comma)
fruits = ("apple",)
print("Single-element tuple:", fruits, "| Type:", type(fruits))
print("Repetition (fruits * 3):", fruits * 3, "| Type:", type(fruits))
print("-" * 40)

# 4. Creating Tuple using Constructor tuple()
stu_info = tuple(["Alice", 15, 23000, True])
print("stu_info:", stu_info, "| Type:", type(stu_info))
print("-" * 40)

# 5. Implicit Tuple creation & Immutability
numbers = 1, 2, 3, 4, 5
print("Implicit tuple numbers:", numbers, "| Type:", type(numbers))
# numbers[1] = 200  # TypeError: 'tuple' object does not support item assignment
del numbers
print("-" * 40)

# 6. Tuple Packing & Unpacking
# Unpacking with extended target (*operator)
fruits = ("apple", "banana", "cherry")
f1, *f2 = fruits
print("f1 (first item):", f1)
print("f2 (remaining items as list):", f2, "| Type:", type(f2))

# Packing values into a tuple
a = 10
b = 20
c = 30
numbers = (a, b, c)
print("Packed tuple numbers:", numbers, "| Type:", type(numbers))
print("-" * 40)

# 7. Tuple Concatenation
a = (1, 2, 3)
b = (5, 6, 7, 8)
c = a + b
print("Concatenated tuple c:", c, "| Type:", type(c))
