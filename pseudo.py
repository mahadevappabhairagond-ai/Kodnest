# To Print Hello world
print("Hello world Thank you for learning python")
print("Hello world \n Thank you for learning python")
print("Hello world " , end=" ")
print("Thank you for learning python")
# To find wheather number (n) is even or odd
'''
start
 input n
 if n%2 == 0
     print("even")
 else
    print("odd")
end
'''

# To find the number is pos , neg or zero
'''
start
input n
if n>=0:
    print("positive")
:else if n<0
    print("negative")
else
   print("zero")
   end
'''
# To find the largest among 3 numbers a, b, c
'''
start
input a,b,c
if a>=b and a>=c:
    print(a)
else if b>=a and b>=c:
    print(b)
else:
    c>=a and c>=b:
    print(c)
    end
'''

print("Hello world")



n = int(input("Enter a number: "))
if n%2==0:
    print("Even")
else:
    print("odd")


num = int(input("Enter a number to check (+/-/0): "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

if a >= b and a >= c:
    print(f"Largest is {a}")
elif b >= a and b >= c:
    print(f"Largest is {b}")
else:
    print(f"Largest is {c}")







