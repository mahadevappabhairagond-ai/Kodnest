# {key:value}, mutable, key cannot be duplicated

student = {
    "name": "Mahadev",
    "name": "Rahul",
    "age": 22,
    "gender": "Male",
    "course": "Computer Science",
    "Tech": ["Computer Science", "Python", "SQL"]

}
student["age"] = 25
student.update({'cgpa' : 8.5})
print(student["age"])
print(student, type(student), len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))

print(student.pop("course"))
student.popitem() # last item
student.clear() # remove all items
del student
# print(student)

student = {
    "name": "Rahul",
    "age": 23,
    "Tech": ["Python", "SQL"]
}

student.setdefault("age", 22)
print(student)

keys = ["name", "age", "course"]
y = 0

student = dict.fromkeys(keys, y)
print(student)

my_dict = student.copy()
print(my_dict)
my_dict.update({'name': "Amit"})
print(my_dict)

student = {
    "name": "Rahul",
    "language": "java",
    "marks": 88
}
for x in student:
    print(f"{x} => {student[x]}")

for x in student.items():
    print(x)

for x in student.keys():
    print(x)

for x in student.values():
    print(x)

# Nested Dictionary

students = {
    "stul": {
        "name": "Rahul",
        "age": 23,
        "Tech": ["Python", "SQL"]
    },
    "stu2": {
        "name": "Mahadev",
        "age": 22,
        "Tech": ["Java", "SQL", "Python"]
    }
    
}

print(students)
print(students["stu2"]["name"])

for x in students:
    print(x)
    for y in students[x]:
        print(y, students[x][y])
