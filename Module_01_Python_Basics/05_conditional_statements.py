# 05 - Conditional Statements in Python
# ------------------------------------------------------------

# 1. Simple If-Else Statement
# Task: Check whether a person is eligible to vote (age >= 18)
print("=== 1. Voting Eligibility Check ===")
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print("Thank You!\n")


# 2. If-Elif-Else Statement
# Task: Grade assignment based on marks (>=90: A, >=70: B, >=50: C, >=35: D, <35: Fail)
print("=== 2. Grade Assignment ===")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
print()


# 3. Nested If Statement
# Task: Check if free tonight and friends are available to party
print("=== 3. Nested Decision Making ===")
free_tonight = True
friends_available = True

if free_tonight:
    if friends_available:
        print("Go out for party")
    else:
        print("Sit and watch a movie at home")
else:
    print("Not available for party")
print()


# 4. Match-Case Statement (Python 3.10+)
# Task: Accept a number from 1 to 7 and print the corresponding day of the week
print("=== 4. Day of the Week (Match-Case) ===")
day = int(input("Enter a number between 1 to 7: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
print()


# 5. Match-Case with Multiple Patterns
# Task: Accept a month number and print the season: 3,4,5 -> Summer, 6,7,8 -> Rainy, 9,10,11,12 -> Winter
print("=== 5. Season Identifier (Match-Case Multiple Patterns) ===")
month = int(input("Enter a month number (1-12): "))
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11 | 12:
        print("Winter")
    case _:
        print("Invalid month number")
