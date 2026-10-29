# Inbuilt String Methods - single Program
s = "  Kodnest Technologies 123  "
print("Original String:", s)

# Case conversion methods
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())

# Searching & counting
print("find('Tech'):", s.find("Tech"))
print("count('o'):", s.count("o"))

# Replace
print("replace('123', '2025'):", s.replace("KodNest", "2025"))

# Strat & End check
print("startswith('  Kod'):", s.startswith("  Kod"))
print("endswith('123  '):", s.endswith("123  "))

# Split & Join
words = s.split()
print("split():", words)
print("join():", "_".join(words))

# Strip spaces
print("isalpha():", s.isalpha())
print("isdigit():", s.isdigit())
print("isspace():", s.isspace())
print("isalnum():", s.isalnum())
print("Hello". isalnum())

# Length
print("Length of string:", len(s))

