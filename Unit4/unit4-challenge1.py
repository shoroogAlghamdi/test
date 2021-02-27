# Slide 55

tsherts = eval(input("How many T-sherts you want to buy? "))
pants = eval(input("How many pants do you want to buy? "))
shoes = eval(input("How many pair of shoes do you want to buy? "))

if tsherts == 2 or pants == 2:
    print("You will have a 15% discount!")
elif tsherts == 1 and pants == 1:
    print("You will have a 15% discount!")
elif (tsherts==1 or pants==1) and not (shoes>0):
    print("You will have a 15% discount!")
else:
    print("Sorry, there is NO discount on the pieces you have taken!")