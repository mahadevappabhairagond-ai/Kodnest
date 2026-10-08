# 03 - Inbuilt String Methods in Python
# ------------------------------------------------------------

s = "  Kodnest Technologies 123  "
print("Original String:", repr(s))
print("-" * 40)

# 1. Case Conversion Methods
print("=== Case Conversion ===")
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())
print("-" * 40)

# 2. Searching & Counting
print("=== Searching & Counting ===")
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))
print("-" * 40)

# 3. Replacing Substrings
print("=== Replace ===")
print("replace('123', '2025'):", s.replace("123", "2025"))
print("-" * 40)

# 4. Start & End Verification
print("=== Start & End Checks ===")
print("startswith('  Kod'):", s.startswith("  Kod"))
print("endswith('123  '):", s.endswith("123  "))
print("-" * 40)

# 5. Splitting & Joining
print("=== Split & Join ===")
words = s.split()
print("split():", words)
print("join('_'):", "_".join(words))
print("-" * 40)

# 6. Character Classification Methods
print("=== Character Validation ===")
print("s.isalpha():", s.isalpha())
print("s.isdigit():", s.isdigit())
print("s.isspace():", s.isspace())
print("s.isalnum():", s.isalnum())
print("'Hello'.isalnum():", "Hello".isalnum())
print("-" * 40)

# 7. String Length
print("=== Length ===")
print("Length of string:", len(s))
