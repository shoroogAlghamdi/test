# Slide 28
height = eval(input("Enter your height in CM: "))
weight = eval(input("Enter your weight in KG: "))
if height > 165 and weight < 50:
    print("You definitely gonna be a great model! You must look for a modeling agency!")
elif height  > 165 and weight > 50:
    print("You need to follow a deight! Models never eat carbs or  sugar :)")
elif height < 165 and weight < 50:
    print("You might be a great choice to model Petite!")
else:
    print("I am sorry! You should find another job for yourself far far away from modeling!")