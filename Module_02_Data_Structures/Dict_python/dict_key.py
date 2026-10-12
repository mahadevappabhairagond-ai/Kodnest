
list_prod = ["Apple", "Banana", "Chechu", "DragonFruit"]

products = {
     "Apple": ["Fresh Apple", 120],
     "Banana": ["Ripe Banana", 60],
     "Chechu": ["Chechu Fruit", 80],
     "DragonFruit": ["Dragon Fruit", 150]
}

print(products[list_prod[0]][0])  # Output: Fresh Apple
print(products[list_prod[1]][0])  # Output: Ripe Banana
  
                                  

# employee id

employees = [
    {"employee_id": "E101", "name": "Mahadev", "age": 22},
    {"employee_id": "E102", "name": "Rahul", "age": 23},
    {"employee_id": "E103", "name": "Amit", "age": 24}
]

print(employees)

employee_by_id = {}

for employee in employees:
    employee_id = employee["employee_id"]
    employee_by_id[employee_id] = employee

print(employee_by_id)

