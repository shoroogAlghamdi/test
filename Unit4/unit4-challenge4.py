# slide 118
password = input("Enter your password: ")

smallLetter = False
capitalLetter = False
digit = False
isCharacter = False
validLength = False

for element in password:
    if element.isdigit():
        digit = True
    if element.islower():
        smallLetter = True
    if element.isupper():
        capitalLetter = True
    if element == "$" or element == "#" or element == "@":
        isCharacter = True

if(len(password)>=6 and len(password)<=16):
     validLength = True

if smallLetter == True and capitalLetter == True and digit == True and isCharacter == True and validLength == True:
    print("Your password is so strong! No one can figure it out!")
elif smallLetter == False:
    print("Try to add lowercase letters to your password!")
elif capitalLetter == False:
    print("Try to add uppercase letters to your password!")
elif digit == False:
    print("Try to add numbers [0-9] to your password!")
elif isCharacter == False:
    print("Try to add characters like #,@,$ to increase the complixity of your password!")
elif validLength == False:
    print("Your password is eaither too short or too long, make it between 6 and 16!")
else:
    print("You should look for a stronger password!")
