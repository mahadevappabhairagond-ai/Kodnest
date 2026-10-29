class student:
    # class attr - classname or obj ref
    company = "Kodnest Technologies"
    # Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    # Instance method - using self reference, obj ref
    def study(self):
    #  a = 10 # local attributes
    # print(a)
        print(f"{self.name} is studying")


    
    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)

    def trip(self):
        print(f"{self.name} is going for a trip")

s1 = student("Mahadev",23)
print(student.company)
print(s1.company)
print(s1.name)
s1.study()
s1.getDetails()
s1.trip()

print("\n")
s2 = student("Mahadev",24)
print(s2.name)
s2.study()
s2.getDetails()
s2.trip()





    
