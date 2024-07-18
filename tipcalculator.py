print("Welcome to the tip calculator.")
tot=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people=int(input("How many people to split the bill? "))
tipamount=tot*(tip/100)
tipamount+=tot
per_person=round(tipamount/num_of_people,2)
print(f"Each person should pay: $ {per_person}")
