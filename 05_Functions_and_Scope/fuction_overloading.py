# 1) default arguments
def add(a,b = 0, c = 0, d = 10):
    return a + b + c + d


print(add(2,3))       # 5
print(add(2,3,4))     # 9
print(add(2,3,4,5))   # 14

# 2) * args or var-args (variable arguments)

def add(*a):
    return a

print(add(10, 20, 30, 40, 50))
print(type(add(10, 20, 30, 40, 50)))

def add(*args):
    total = 0
    for i in args:
        total = i  # total = total + i
        return total

print(add(10, 20))
print(add()) # 0

