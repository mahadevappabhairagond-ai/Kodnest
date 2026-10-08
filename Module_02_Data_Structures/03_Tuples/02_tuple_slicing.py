# 02 - Tuple Slicing Practice Questions (30 Exercises)
# ============================================================

# Exercise 1: Positive slice with start and stop
t = (10, 20, 30, 40, 50)
print("Q1:", t[1:4])

# Exercise 2: Slice from beginning
t = (10, 20, 30, 40, 50)
print("Q2:", t[:3])

# Exercise 3: Slice to the end
t = (10, 20, 30, 40, 50)
print("Q3:", t[2:])

# Exercise 4: Negative index slice to the end
t = (10, 20, 30, 40, 50)
print("Q4:", t[-3:])

# Exercise 5: Slice from index 1 to end
t = (10, 20, 30, 40, 50)
print("Q5:", t[1:])

# Exercise 6: Slice omitting last element
t = (10, 20, 30, 40, 50)
print("Q6:", t[:-1])

# Exercise 7: Step of 2
t = (10, 20, 30, 40, 50, 60)
print("Q7:", t[::2])

# Exercise 8: Step of 3
t = (10, 20, 30, 40, 50, 60, 70)
print("Q8:", t[::3])

# Exercise 9: Reverse tuple
t = (10, 20, 30, 40, 50)
print("Q9:", t[::-1])

# Exercise 10: Reverse slice between indices
t = (1, 2, 3, 4, 5, 6)
print("Q10:", t[4:2:-1])

# Exercise 11: Negative range
t = (10, 20, 30, 40, 50)
print("Q11:", t[-4:-1])

# Exercise 12: Reverse negative range
t = (10, 20, 30, 40, 50)
print("Q12:", t[-1:-4:-1])

# Exercise 13: Odd indexed elements
t = (5, 10, 15, 20, 25, 30)
print("Q13:", t[1::2])

# Exercise 14: Reverse step of 2
t = (5, 10, 15, 20, 25, 30)
print("Q14:", t[::-2])

# Exercise 15: Sub-tuple range
t = (10, 20, 30, 40, 50, 60)
print("Q15:", t[2:5])

# Exercise 16: Step of 3
t = (10, 20, 30, 40, 50, 60, 70)
print("Q16:", t[::3])

# Exercise 17: Range with step 2
t = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print("Q17:", t[1:7:2])

# Exercise 18: Negative start with positive step
t = (10, 20, 30, 40, 50, 60)
print("Q18:", t[-5:-1:2])

# Exercise 19: Negative step of -2
t = (10, 20, 30, 40, 50)
print("Q19:", t[-1:-5:-2])

# Exercise 20: Full shallow copy of tuple
t = (10, 20, 30)
new_t = t[:]
print("Q20:", new_t)

# Exercise 21: Empty slice (same start and stop)
t = (10, 20, 30, 40)
print("Q21:", t[2:2])

# Exercise 22: Out of bound stop index
t = (10, 20, 30, 40)
print("Q22:", t[1:100])

# Exercise 23: Out of bound start index
t = (10, 20, 30, 40)
print("Q23:", t[100:])

# Exercise 24: Reverse step single step
t = (10, 20, 30, 40, 50, 60)
print("Q24:", t[5:4:-1])

# Exercise 25: Chained slice reversal
t = (10, 20, 30, 40, 50)
print("Q25:", t[1:4][::-1])

# Exercise 26: Double slice indexing
t = (10, 20, 30, 40, 50, 60)
result = t[1:5][1:3]
print("Q26:", result)

# Exercise 27: Slicing tuple of strings
t = ("Java", "Python", "C++", "JavaScript", "SQL")
print("Q27:", t[1:4])

# Exercise 28: Slicing nested tuple
t = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print("Q28:", t[1][0:2])

# Exercise 29: Negative reverse range
t = (1, 2, 3, 4, 5, 6, 7)
print("Q29:", t[-2:-6:-1])

# Exercise 30: Reverse step on 8-element tuple
t = (10, 20, 30, 40, 50, 60, 70, 80)
print("Q30:", t[::-2])
