# 02 - List Mutation vs Reassignment in Python
# ------------------------------------------------------------

# 1. Modification / In-place Mutation
# When two variables reference the same list object, modifying one affects both.
marks = [70, 81, 60]
stu_marks = marks
stu_marks[0] = 100

print("marks:", marks)          # [100, 81, 60]
print("stu_marks:", stu_marks)  # [100, 81, 60]
print("-" * 40)

# 2. Reassignment
# Reassigning points the variable to a new object, leaving the original intact.
num = [10, 20]
values = num
values = [100, 200]

print("num:", num)        # [10, 20]
print("values:", values)  # [100, 200]
print("-" * 40)

# 3. Difference: Identity (is) vs Equality (==)

# Case A: Aliasing (same object reference)
first = [1, 2, 3]
second = first
print("Aliased - first is second:", first is second)  # True
print("Aliased - first == second:", first == second)  # True

# Case B: Reassignment / Separate objects with identical values
first = [1, 2, 3]
second = [1, 2, 3]
print("Separate - first is second:", first is second)  # False (different memory)
print("Separate - first == second:", first == second)  # True (same content)
