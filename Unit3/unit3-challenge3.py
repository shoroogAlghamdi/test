# Slide 81
height, weight = eval(input("Enter your height in CM and your weight in KG (Seperated by a comma): "))
height2 = height / 100
bmi = weight / (height2 * height2)
print("The BMI of a body with height", height, " and weight", weight, " is ", bmi)
