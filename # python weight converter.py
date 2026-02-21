# python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilogram or pounds? (K or L): ")

if unit == "K":
    weight = weight *4
    print(weight)
elif unit =="L": 
   weight = weight/4.5
   unit = "kgs."
else:
    print(f"{unit} was not valid") 

    print(f"Your new weight is: {weight} {unit}")    