
# marksMass= 78
# johnsMass=92 
# marksHeight=1.69
# johnsHeight=1.95

# def BMI(mass,height):
#     return mass/height**2
# print(BMI(marksMass,marksHeight))
# print(BMI(johnsMass,johnsHeight))
# print(BMI(95,1.88))
# print(BMI(85, 1.76))

# markHigherBMI=BMI(marksMass,marksHeight) > BMI(johnsMass,johnsHeight)
# print(markHigherBMI)

# if BMI(marksMass,marksHeight) > BMI(johnsMass,johnsHeight):
#     print("Mark's BMI is higher than John's!")
# else:
#     print("John's BMI is higher than Mark's!") 

# if BMI(marksMass,marksHeight) > BMI(johnsMass,johnsHeight):
#     print(f"Mark's BMI {BMI(marksMass,marksHeight)} is higher than John's{BMI(johnsMass,johnsHeight)}!")
# else:
#     print(f"John's BMI{BMI(johnsMass,johnsHeight)} is higher than Mark's{BMI(marksMass,marksHeight)}!") 


# marksMass= 95
# johnsMass=85
# marksHeight=1.88
# johnsHeight=1.76

# marksBMI = marksMass / marksHeight**2
# print(marksBMI)

# johnsBMI=johnsMass/johnsHeight**2
# print(johnsBMI) 
 
# markHigherBMI=marksBMI>johnsBMI
# print(markHigherBMI)




class Email:
    def __init__(self, name):
        self.name= name
    
    def domain(self):
        return f'{self.name} @ gmail.com'
    
firstEmail= Email('Jack')

secondEmail= Email('Kwame')

print(firstEmail.domain())
print(secondEmail.domain())