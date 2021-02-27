# Slide 38

# Step 1: Obtain inputs from user
height = input("Enter your height in CM: ")
weight = input("Enter your weight in KG: ")

# Step 2: Convert strings to integers
height = eval(height)
weight = eval(weight)

# Step 3: Convert CM to M
height2 = height/100

# Step 4: Calculate the BMI
bmi = weight/(height2*height2)

# Step 5: Display the result
print("The BMI of a body with height ", height, "and weight ", weight, "is" , bmi)
