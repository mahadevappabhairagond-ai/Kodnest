# If & else statement 
# Write a python program to check whether a person is eligible to vote. if the age is 18 or above. print "Eligible to vote"

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")

else:
    print("Not eligible to vote")
print("Thank You!")

# if-elif-else statement
# write a python program to check whether you are free tonight. if you are free. check whether your friends are
# getting marks like a 90-A, 70-B, 50-C, 35-D, <35-F

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

# Nested if statement
# print "Go out for party" if both are true: otherwise print the appropriate message.print

free_tonight = True
friends_available = True
if(free_tonight):
    if(friends_available):
        print("Go out for party")
    else:
        print("seat and watch the movie at home")
else:
    print("not available for party")


# match_case statement
# Write a python program that accepts a number from 1 to 7 and uses match-case to print the corresponding day of the week

day = int(input("Enter a number between 1 to 7: "))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: 
        print("Invalid")

# match case with multiple casess
# Write a python program that accepts a month number and uses match case to print the season: 3,4,5 -> summer, 6,7,8 -> Rainy, 9,10,11,12 -> winter

month = int(input("Enter a month number: "))
match month:
    case 3 |4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11:
        print("Winter")
    case _:
        print("Invalid")