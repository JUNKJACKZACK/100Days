print("Welcome to the auction!")


bidder1 = int(input("Bidder number one what is your bid going to be? $"))
bidder2 = int(input("Bidder number two what is your bid going to be? $"))
bidder3 = int(input("Bidder number three what is your bid going to be? $"))
bidder4 = int(input("Bidder number four what is your bid going to be? $"))

if bidder1 > bidder2:
    bidder1 = print(f"{bidder1} is the highest bidder")
elif bidder2 > bidder1:
    bidder2 = print(f"{bidder2} is the highest bidder")
elif bidder3 > bidder2:
    bidder1 = print(f"{bidder1} is the highest bidder")
elif bidder2 > bidder3:
    bidder1 = print(f"{bidder1} is the highest bidder")