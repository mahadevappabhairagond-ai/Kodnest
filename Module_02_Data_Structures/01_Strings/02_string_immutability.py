# 02 - String Immutability and Object Identity in Python
# ------------------------------------------------------------

# 1. Strings are Immutable: Modifying creates a new object in memory
s1 = "hello"
print("Initial s1:", s1, "| Memory ID:", id(s1))

s1 = s1 + "world"
print("Modified s1:", s1, "| Memory ID (changed):", id(s1))
print("-" * 40)

# 2. Comparison: String interning and concatenation identity
s1 = "hello"
s2 = s1 + "world"
print("s1:", s1, "| ID:", id(s1))
print("s2:", s2, "| ID:", id(s2))
print("s1 == s2 (Value equality):", s1 == s2)
print("s1 is s2 (Reference identity):", s1 is s2)
print("-" * 40)

# 3. String Interning: Identical literals share memory reference
s1 = "python"
s2 = "python"
print("s1:", s1, "| ID:", id(s1))
print("s2:", s2, "| ID:", id(s2))
print("s1 == s2 (Value equality):", s1 == s2)
print("s1 is s2 (Reference identity):", s1 is s2)
