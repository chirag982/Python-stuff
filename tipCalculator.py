print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12, or 15? "))
people_split = int(input("How many people to split the bill? "))
final_bill = float(total_bill + ((tip*total_bill)/100))
each = float(final_bill/people_split)
print(f"Each person has to pay ${each}.")
