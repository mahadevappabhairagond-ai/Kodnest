# 04 - String Positive Slicing Practice
# ============================================================
# Syntax:
#   string[start:stop:step]
#
# Rules:
# 1. start is INCLUDED
# 2. stop is EXCLUDED
# 3. Positive step moves from LEFT to RIGHT
# 4. If step is omitted, default step is 1
# ============================================================

# Basic Indexing and Slicing Demo
s1 = "Python"
print("Original:", s1)
print("s1[2]:", s1[2])
print("s1[5]:", s1[5])
print("s1[1:4]:", s1[1:4])
print("s1[0:5]:", s1[0:5])
print("s1[:]:", s1[:])
print("s1[:4]:", s1[:4])
print("s1[2:]:", s1[2:])
print("s1[1:]:", s1[1:])
print("s1[0::1]:", s1[0::1])
print("s1[0::2]:", s1[0::2])
print("s1[1:5:2]:", s1[1:5:2])
print("s1[:3]:", s1[:3])
print("s1[4:]:", s1[4:])
print("s1[::4]:", s1[::4])

print("\n" + "=" * 60)
print("LEVEL 1 - POSITIVE SLICING PRACTICE EXERCISES")
print("=" * 60)

text = "Python"
print("1.", text[0:3])  # Expected: Pyt

text = "Programming"
print("2.", text[1:5])  # Expected: rogr

text = "Developer"
print("3.", text[2:6])  # Expected: velo

text = "Computer"
print("4.", text[3:7])  # Expected: pute

text = "Artificial"
print("5.", text[0:4])  # Expected: Arti

text = "Education"
print("6.", text[2:7])  # Expected: ucati

text = "JavaScript"
print("7.", text[4:10])  # Expected: Script

text = "DataScience"
print("8.", text[4:10])  # Expected: Scienc

text = "PythonProgramming"
print("9.", text[:6])  # Expected: Python

text = "PythonProgramming"
print("10.", text[6:])  # Expected: Programming

text = "FullStackDeveloper"
print("11.", text[:9])  # Expected: FullStack

text = "FullStackDeveloper"
print("12.", text[9:])  # Expected: Developer

text = "MachineLearning"
print("13.", text[:7])  # Expected: Machine

text = "MachineLearning"
print("14.", text[7:])  # Expected: Learning

text = "ABCDEFGHIJ"
print("15.", text[0:8:2])  # Expected: ACEG

text = "ABCDEFGHIJ"
print("16.", text[1:9:2])  # Expected: BDFH

text = "ABCDEFGHIJKL"
print("17.", text[0:12:3])  # Expected: ADGJ

text = "ABCDEFGHIJKL"
print("18.", text[2:10:2])  # Expected: CEGI

text = "1234567890"
print("19.", text[0:10:2])  # Expected: 13579

text = "1234567890"
print("20.", text[1:9:2])  # Expected: 2468

text = "Programming"
print("21.", text[0:11:3])  # Expected: Pgmn

text = "Programming"
print("22.", text[1:10:3])  # Expected: rami

text = "PythonProgramming"
print("23.", text[2:14:2])  # Expected: toPorm

text = "PythonProgramming"
print("24.", text[1:15:3])  # Expected: yoPgm

text = "ABCDEFGHIJKLMNO"
print("25.", text[3:13:2])  # Expected: DFHJL

text = "ABCDEFGHIJKLMNO"
print("26.", text[2:14:3])  # Expected: CFIl

text = "PythonProgramming"
print("27.", text[0:16:4])  # Expected: Ponr

text = "ABCDEFGHIJKLM"
print("28.", text[1:12:3])  # Expected: BEHK

text = "DataScienceWithPython"
print("29.", text[4:18:2])  # Expected: ScnewtP

text = "FullStackDevelopment"
print("30.", text[2:19:3])  # Expected: ltkvpe

text = "Python"
print("31.", text[1:5])    # Expected: ytho
print("32.", text[1:5:1])  # Expected: ytho
print("33.", text[1:5:2])  # Expected: yh
print("34.", repr(text[4:2]))   # Expected: '' (empty string because step is positive but start > stop)
print("35.", repr(text[2:2]))   # Expected: ''
print("36.", repr(text[10:20])) # Expected: ''
print("37.", text[0:100])  # Expected: Python

text = "ABCDEFGHIJKLM"
print("38.", text[2:11:3])  # Expected: CFI

text = "ProgrammingLanguage"
print("39.", text[3:15:2])  # Expected: gamnLa

text = "PythonDeveloper"
print("40.", text[1:12:3])  # Expected: yoee

text = "DataScience"
print("41.", text[0:10:2])  # Expected: DtSin

text = "FullStackDeveloper"
print("42.", text[4:16:2])  # Expected: Sackev
