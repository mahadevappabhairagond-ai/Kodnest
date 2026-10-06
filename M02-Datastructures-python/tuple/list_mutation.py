# Modification/Mutation

marks = [70, 81, 60]
stu_marks = marks
stu_marks[0] = 100
print(marks)
print(stu_marks)

# Reassignment

num = [10, 20]
values = num
values = [100, 200]
print(num)
print(values)

# diff in reassignment and mutation
# mutation
first = [1, 2, 3]
second = first
print(first is second)
print(first == second)

# Reassignment
first = [1, 2, 3]
second = [1, 2, 3]
print(first is second)
print(first == second)