# Slide 177
# Obtain current salary
salaryBeforeBonus = eval(input("Please, enter your current salary: "))
# Obtain the rank
isManager = input("Are you a manager? (yes/no): ")
bonus = 0 # Initialize
# Decide the bonus depending on the rank
if isManager == "yes":
    bonus = 2000
else:
    bonus = 1000
# Calculate the salary
salaryAfterBonus = salaryBeforeBonus + bonus
# Show final salary
print("Your salary after adding a bonus of", bonus, "SR is", salaryAfterBonus)

