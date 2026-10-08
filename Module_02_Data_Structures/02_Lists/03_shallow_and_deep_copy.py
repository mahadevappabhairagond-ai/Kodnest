# 03 - Shallow Copy vs Deep Copy in Python
# ------------------------------------------------------------
import copy

# 1. Normal Assignment (Reference Copy)
# Both variables point to the exact same memory address.
print("=== 1. Normal Assignment (Reference Copy) ===")
original = [[10, 20], [30, 40]]
copy_ref = original
copy_ref[0][0] = 100

print("copy_ref:", copy_ref)  # [[100, 20], [30, 40]]
print("original:", original)  # [[100, 20], [30, 40]]
print("-" * 40)


# 2. Shallow Copy (.copy())
# Copies outer list structure, but inner nested objects are still referenced.
print("=== 2. Shallow Copy ===")
original = [[10, 20], [30, 40]]
shallow_cpy = original.copy()
shallow_cpy[0][0] = 100

print("shallow_cpy:", shallow_cpy)  # [[100, 20], [30, 40]]
print("original:   ", original)     # [[100, 20], [30, 40]] (affected because nested list is shared!)
print("-" * 40)


# 3. Deep Copy (copy.deepcopy())
# Recursively duplicates all objects and nested lists completely independently.
print("=== 3. Deep Copy ===")
original = [[10, 20], [30, 40]]
deep_cpy = copy.deepcopy(original)
deep_cpy[0][0] = 100

print("original:", original)  # [[10, 20], [30, 40]] (unaffected!)
print("deep_cpy:", deep_cpy)  # [[100, 20], [30, 40]]
