# Slide 109


name = input("Enter your name: ")
numberOfLetters = len(name)-1
soulMate = ""
while numberOfLetters >= 0:
     soulMate += name[numberOfLetters]
     numberOfLetters = numberOfLetters -1
print("Your soulmate name is ", soulMate, "!")
