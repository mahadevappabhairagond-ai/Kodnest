c = 30
def add():
    global a
    a = 10
    b = 20 # local variable
    print(a + b)
    print(c) # global variable 
add()
print(c)
# print(f"The value of a is {a}") # global variable
# print(a + b)

x = 100 # global variable
def display():
    x = 50 # local
    print("Local x:", x) # 50
display()
print("Global x:", x) # 100

x = 10 # global variable
def display():
    print(x)
    # x = 20 # local variable
display()
x = 20
print(x)