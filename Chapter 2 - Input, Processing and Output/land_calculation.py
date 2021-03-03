# 3. Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
# enter the total square feet in a tract of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43,560 to get the number of acres.

#Display introductory message
print("Welcome to Square feet to Acre Land Calculation Converter ......\n")

#Get the total square feet of the land
total_square_feet = float(input("Enter the total square feet: "))

#Calculate the number of acres, note: 1 acre = 43,560square feet
acres = int(total_square_feet // 43560)

#Calculate the remaining square feet
square_feet = int(total_square_feet % 43560)

print(f"The land is {acres} acres, {square_feet} sq ft")


