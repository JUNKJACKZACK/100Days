print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15 ")
people = input("How many people to split the bill? ")
tipped_amount = float(total) * (1 + int(tip_percentage) / 100)
total_per_person = tipped_amount / int(people)
print(f"Each person should pay: ${total_per_person}")