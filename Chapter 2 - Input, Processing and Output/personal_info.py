#1. Personal Information
#   Write a program that displays the following information:
#       • Your name
#       • Your address, with city, state, and ZIP
#       • Your telephone number
#       • Your college major

#Request for personal information
name = input("Enter your full name: ")
address = input("Enter your address: ")
city = input("Enter the city: ")
state = input("Enter the state: ")
major = input("Enter your college major: ")

print(f"\nBelow are your details as submitted:\n Name: {name}\n Address: {address}, {city}, {state}\n College Major: {major}")
