import copy

# 1. Normal assignment(not a copy)

original = [[10, 20],[30, 40]]
copy_ref = original
copy_ref[0][0] = 100
print(copy_ref) # 100, 20 / 30, 40
print(original)  # 100, 20 / 30, 40

# 2. shallow copy

original = [[10, 20], [30, 40]]
shallow_cpy = original.copy()
shallow_cpy[0][0] = 100
print(shallow_cpy) # 100, 20 / 30, 40
print(original) # 100, 20 / 30, 40

# 3. deep copy

original = [[10, 20], [30, 40]]
cpy_list = copy.deepcopy(original)
cpy_list[0][0] = 100
print(original) # 10, 20 / 30, 40
print(cpy_list) # 100, 20 / 30, 40 


