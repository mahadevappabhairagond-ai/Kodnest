# Looping statement
for i in range(1,6):
    print(i)

# write a python program to print 0 to 5 using loop
for i in range(5):
     print(i)

# for loop with if condition
# write a python program to print a even number from 1 to 10  using a for loop

for i in range(1,11):
    if i % 2 == 0:
        print(i)

# while loop
# write a python program to print a numbers form 0 to 4 using while loop

i = 0
while i <= 4:
    print(i)
    i += 1  # i = i + 1

# jumping statement
# break statement
# write a python program to print number from 1 to 5, but stop the loop when the number reaches 4.

for i in range(1,6):
    if i == 4:
        break
    print(i)

# Continue statement
# write a python progrm  to print the number form 1 to 5, but skip 3.

for i in range(1,6):
    if i == 3:
        continue
    print(i)

# pass statement
# write a python program using a for loop from 1 to 9 and uses pass statement.
# pass in function

for i in range(1, 10):
    pass

# Write a python program to create a function called add() without parameters

def add():
    pass

# return statement
# write a python function called square(n) that accepts a number from user and return the square of that number.

def square(n):
    return n*n
print(square(3))