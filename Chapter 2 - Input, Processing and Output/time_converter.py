#Get the total seconds from the user
total_seconds = int(input("Enter the total time in seconds: "))

#Get the number of hours
hours = total_seconds // 3600

#Get the number of minutes
minutes = (total_seconds // 60) % 60

#Get the number of seconds
seconds = total_seconds % 60

print(f"The time is: {hours}hr(s): {minutes}min(s): {seconds}sec(s)")