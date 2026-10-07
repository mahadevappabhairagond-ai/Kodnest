# sets are unordered, unindexed and mutable, unchageable
# duplication is not allowed
# they store only unique values

s = {1, 2, 3, 4, 5}
# print(s, s[1])
# s[2] = 300 # sets are immutable
s.add(7)
s.update({6, 8, 9}) # it used for add multiple values inside a set.
s.remove(9)
s.discard(10)
s.pop()
s.clear()
del s
# print(type(s), s)

s1 = {1, 2, 3, "Hello", 1.2, True, 0, 1.2324, 1, 2, False}
print(s1)

# Constructor of set
s2 = set()
print(s2, type(s2)) # empty set
s3 = set([1, 2, 3, 4])
print(s3, type(s3))
s4 = set((1, 2, 3, 4))
print(s4, type(s4))
s5 = set({"Hello": 1, "World": 2})
print(s5, type(s5))
# using loop we can print a values of set
for i in s3:
    print(i)

# Immutable - frozenset
# In the forzenset we cant add a values inside a set

fs = frozenset([1, 2, 3])
print(fs, type(fs))
#fs.add(6)