# This script will create a little intro for you based on your input

firstName=input("Enter your first name: ")
lastName=input("Enter your last name: ")
age=int(input("Enter your age as an integer: "))
program=input("What program are you studying? ")

intro=("\nIntroduction:\n\nMy name is "+firstName+" "+lastName+"\nI am "+str(age)+" years old\nI am part of the "+program+" program:)")
print(intro)