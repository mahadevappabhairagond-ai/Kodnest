# 01 - Set Basics & Operations in Python
# ------------------------------------------------------------
# Properties of Sets:
# - Unordered collection (items do not have a defined order)
# - Unindexed (cannot access items via index like s[0])
# - Unique elements only (automatically removes duplicates)
# - Mutable (can add/remove elements), but set elements must be hashable/immutable
# ------------------------------------------------------------

# 1. Basic Set Creation and In-place Modifications
s = {1, 2, 3, 4, 5}
print("Initial set s:", s)

s.add(7)
print("After add(7):", s)

s.update({6, 8, 9})  # Add multiple elements
print("After update({6, 8, 9}):", s)

s.remove(9)  # Raises KeyError if not found
print("After remove(9):", s)

s.discard(10)  # Does NOT raise error if 10 not found
print("After discard(10):", s)

popped = s.pop()  # Removes an arbitrary element
print(f"After pop() [removed {popped}]:", s)

s.clear()
print("After clear():", s)

del s
print("-" * 40)

# 2. Duplicate Filtering & Heterogeneous Datatypes
# Note: In Python, True == 1 and False == 0, so only one is kept.
s1 = {1, 2, 3, "Hello", 1.2, True, 0, 1.2324, 1, 2, False}
print("Set s1 (duplicates automatically removed):", s1)
print("-" * 40)

# 3. Creating Sets using Constructors
s2 = set()  # Empty set ({} creates an empty dict)
print("s2 (empty set):", s2, "| Type:", type(s2))

s3 = set([1, 2, 3, 4])
print("s3 from list:", s3, "| Type:", type(s3))

s4 = set((1, 2, 3, 4))
print("s4 from tuple:", s4, "| Type:", type(s4))

s5 = set({"Hello": 1, "World": 2})  # Set from dict keys
print("s5 from dict keys:", s5, "| Type:", type(s5))
print("-" * 40)

# 4. Iterating through a Set
print("Iterating over s3:")
for item in s3:
    print(item)
print("-" * 40)

# 5. Immutable Sets: frozenset()
# Frozensets cannot be modified after creation
fs = frozenset([1, 2, 3])
print("frozenset fs:", fs, "| Type:", type(fs))
# fs.add(6)     # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
