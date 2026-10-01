number = [1,2,3,4,5,3]
print(number, type(number))
print(len(number))
print(number[3])
print(number[1:5])
print(number[3:])
print(number[-4:-1])
print(number[-1:-5:-1])
print(number[-1::-1])


# Using Constructor
stu = list(["Abhi", 45, 86.5, True])
print(stu, type(stu))
stu.append("Kodnest")
print(stu)

# adding elements
num = [1, 2, 3, 4, 5]
num.append(6)
print(num)
num.extend([7, 8, 9])
print(num)
num.insert(2, 10)
print(num)
num.insert(10, 20)
print(num)

# removing the element
num.pop()
num.pop(2)
num.remove(7)
num.clear()
del num
#print(num)

# changing element
numbers= [1,2,3,4,5,3]
numbers[5]=6
numbers[1:4] = [20,30,40,50]
print(numbers)
