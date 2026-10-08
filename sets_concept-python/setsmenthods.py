set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2)) # {1,2,3,4,5,6,7,8}
print(set1 | set2) # {1,2,3,4,5,6,7,8}
print(set1.intersection(set2)) # {4,5}
print(set1 & set2) # {4,5}

print(set1.isdisjoint(set2)) # False
print(set1.issuperset(set2)) # False
print(set1.issubset(set2)) # False

print(set1.union(set2)) # {1,2,3,4,5,6,7,8}
print(set1.difference(set2)) # {1,2,3}
print(set1 - set2) # {1,2,3}
print(set2.difference(set1)) # {6,7,8}
print(set2 - set1) # {6,7,8}
print(set1.symmetric_difference(set2)) # {1,2,3,6,7,8}
print(set1 ^ set2) # {1,2,3,6,7,8}

set1.add(6)
print(set1) # {1,2,3,4,5,6}

print(set2 - set1) # {7,8}
print(set1.symmetric_difference(set2)) # {1,2,3,6,7,8}
print(set1 ^ set2) # {1,2,3,6,7,8}

set1.add(6)
print(set1) # {1,2,3,4,5,6}

set1.update(set2)
print(set1) # {1,2,3,4,5,6,7,8}

set1.remove(6)
print(set1) # {1,2,3,4,5,7,8}

set1.discard(6)
print(set1) # {1,2,3,4,5,7,8}

set1.pop()
print(set1) # {1,2,3,4,5,7}

set1.clear()
print(set1) # {}

print(set1, len(set1)) # {} 0