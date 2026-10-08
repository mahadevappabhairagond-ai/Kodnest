# 01 - List Operations & Methods in Python
# ------------------------------------------------------------

# 1. List Creation, Counting & Slicing
numbers = [1, 2, 3, 4, 5, 3]
print("numbers:", numbers)
print("count(3):", numbers.count(3))
print("type:", type(numbers))
print("length:", len(numbers))
print("numbers[3]:", numbers[3])
print("numbers[1:5]:", numbers[1:5])
print("numbers[3:]:", numbers[3:])
print("numbers[-4:-1]:", numbers[-4:-1])
print("numbers[-1:-5:-1]:", numbers[-1:-5:-1])
print("numbers[-1::-1]:", numbers[-1::-1])
print("-" * 40)

# 2. Creating List using Constructor list()
student = list(["Abhi", 45, 86.5, True])
print("student:", student, "| Type:", type(student))
student.append("Kodnest")
print("After append:", student)
print("-" * 40)

# 3. Adding Elements: append(), extend(), insert()
num = [1, 2, 3, 4, 5]
num.append(6)
print("After append(6):", num)

num.extend([7, 8, 9])
print("After extend([7, 8, 9]):", num)

num.insert(2, 10)  # Insert 10 at index 2
print("After insert(2, 10):", num)

num.insert(10, 20)  # Insert 20 at index 10
print("After insert(10, 20):", num)
print("-" * 40)

# 4. Removing Elements: pop(), remove(), clear(), del
print("Before removal:", num)
num.pop()        # Removes last item
print("After pop():", num)

num.pop(2)       # Removes item at index 2
print("After pop(2):", num)

num.remove(7)    # Removes first occurrence of value 7
print("After remove(7):", num)

num.clear()      # Clears all items
print("After clear():", num)

del num          # Deletes the variable completely
print("-" * 40)

# 5. Modifying Elements & Slices
nums = [1, 2, 3, 4, 5, 3]
nums[5] = 6
nums[1:4] = [20, 30, 40, 50]
print("After modifications:", nums)
print("-" * 40)

# 6. Copying and Searching
a = [1, 2, 3]
b = a.copy()
print("Copied list b:", b)
print("Index of 3 in b:", b.index(3))
print("-" * 40)

# 7. Sorting and Reversing
x = [1, 3, 2, 6, 8, 30, 29]
x.sort()
print("Sorted x (ascending):", x)
x.reverse()
print("Reversed x:", x)

sample_list = [1, 3, 2]
sample_list.sort(reverse=True)
print("Descending sort:", sample_list)

sample_list.sort(reverse=False)
print("Ascending sort:", sample_list)
