# Slide 51
today = input("Enter the day: ")
workout = input("Will you workout today (True/False)? ")
run = input("Will you run today (True/False)? ")
workHours = eval(input("How many hours is your schedule today? "))

if today == "Sunday" and workout == "True":
    print("Outfit Recommender: Prepare your swimsuit AND your workout clothes!")
elif (today == "Monday" or today == "Wednesday") and workHours > 8:
    print("Outfit Recommender: You should wear your usual school uniform and prepare your backpack!")
elif today == "Tuesday" and not(run=="True"):
    print("Outfit Recommender: Do not forget to bring your magical hat!")
elif today == "Thursday" :
    print("Outfit Recommender: Time to dance, wear your favorite dress!")
elif today=="Tuesday" and run == "True":
    print("Outfit Recommender: Wear your sneakers!")
else:
    print("This case is not considered!")
