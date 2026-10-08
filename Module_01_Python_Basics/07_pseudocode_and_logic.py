# 07 - Pseudocode, Basic Algorithms & Output Formatting
# ------------------------------------------------------------

# 1. Print Formatting Variations
print("Hello world Thank you for learning python")
print("Hello world \nThank you for learning python")
print("Hello world ", end=" ")
print("Thank you for learning python")
print("-" * 40)


# 2. Check Whether a Number is Even or Odd
"""
Algorithm / Pseudocode:
-----------------------
START
  INPUT n
  IF n % 2 == 0 THEN
      PRINT "Even"
  ELSE
      PRINT "Odd"
END
"""
print("=== 1. Even or Odd Checker ===")
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
print("-" * 40)


# 3. Check Whether a Number is Positive, Negative, or Zero
"""
Algorithm / Pseudocode:
-----------------------
START
  INPUT num
  IF num > 0 THEN
      PRINT "Positive"
  ELSE IF num < 0 THEN
      PRINT "Negative"
  ELSE
      PRINT "Zero"
END
"""
print("=== 2. Positive, Negative, or Zero Checker ===")
num = int(input("Enter a number to check (+/-/0): "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print("-" * 40)


# 4. Find the Largest Among Three Numbers (a, b, c)
"""
Algorithm / Pseudocode:
-----------------------
START
  INPUT a, b, c
  IF a >= b AND a >= c THEN
      PRINT a
  ELSE IF b >= a AND b >= c THEN
      PRINT b
  ELSE
      PRINT c
END
"""
print("=== 3. Largest of Three Numbers ===")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

if a >= b and a >= c:
    print(f"Largest is: {a}")
elif b >= a and b >= c:
    print(f"Largest is: {b}")
else:
    print(f"Largest is: {c}")
