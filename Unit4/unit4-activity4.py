# Slide 67

numberOfChildren = eval(input("Enter number of your children: "))
if numberOfChildren == 2:
    firstChildAge = eval(input("Enter your first child age: "))
    secondChildAge = eval(input("Enter your second child age: "))
    haveCoupon = input("Do you have a coupon (yes/no)? ")
    if firstChildAge < 7 and secondChildAge < 7:
        if haveCoupon == "yes":
            print("Pay nothing, you can enter for free!")
        else:
            print("Pay 5 dollars only!")
else:
    print("We are sorry, we can not offer you a discount!")

