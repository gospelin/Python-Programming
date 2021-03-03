# 3. Age Classifier
# Write a program that asks the user to enter a person’s age. The program should display
# a message indicating whether the person is an infant, a child, a teenager, or an adult.
# Following are the guidelines:
# • If the person is 1 year old or less, he or she is an infant.
# • If the person is older than 1 year, but younger than 13 years, he or she is a child.
# • If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# • If the person is at least 20 years old, he or she is an adult.

#Get the user's age
age = int(input("Enter your age joor: "))

if age <= 1:
    print("You're an infant, small child")
elif age > 1 and age < 13:
    print("You're still a child, but don't give up yet")
elif age > 13 and age < 20:
    print("You are a teenager, soon you will be an adult")
else:
    print("You're an adult..... Hope you are coping well?")
    
    