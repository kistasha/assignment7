# This script will calculate the area of the triangle based on the user's input

base=float(input("Enter the length of the triangle's base: "))
height=float(input("Enter the triangle's height: ")) #changed both to float, because sometimes the area is not int, so that it doesn't round

area=(base * height)/2
print(f"The area of the given triangle is {area}") #upgraded print - removed + str(), included it inside the string itself