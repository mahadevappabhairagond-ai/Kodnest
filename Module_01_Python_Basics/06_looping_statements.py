# 06 - Looping Statements & Functions in Python
# ------------------------------------------------------------

# 1. Basic For Loops
print("=== 1. For Loop (1 to 5) ===")
for i in range(1, 6):
    print(i)

print("\n=== For Loop (0 to 4) ===")
for i in range(5):
    print(i)


# 2. For Loop with Conditional Logic
print("\n=== 2. Even Numbers from 1 to 10 ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 3. While Loop
print("\n=== 3. While Loop (0 to 4) ===")
i = 0
while i <= 4:
    print(i)
    i += 1  # Increment counter


# 4. Jump Statements: Break
# Task: Print numbers 1 to 5, but stop when number reaches 4
print("\n=== 4. Break Statement ===")
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# 5. Jump Statements: Continue
# Task: Print numbers 1 to 5, but skip 3
print("\n=== 5. Continue Statement ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 6. Pass Statement
# Pass acts as a placeholder for future code
print("\n=== 6. Pass Statement ===")
for i in range(1, 10):
    pass  # Loop executes without performing any action


def add():
    """Empty function placeholder using pass."""
    pass


# 7. Functions with Return Statement
# Task: Function square(n) that accepts a number and returns its square
print("\n=== 7. Function Return Statement ===")


def square(n):
    return n * n


result = square(3)
print(f"Square of 3 is: {result}")
