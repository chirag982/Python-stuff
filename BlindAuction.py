import os
print("Welcome to Blind Auction!")
auction = {}

def highest_bid(auction):
    highest_bid = 0 
    for key in auction:
        bid = int(auction[key])
        if bid>highest_bid:
            highest_bid = bid
            highest_bidder = key
    print(f"{highest_bidder} win's! highest bid of ${highest_bid}.")


to_continue = True
while(to_continue):
    os.system('cls')
    name = input("enter the name\n").lower()
    price = input("enter the price\n")
    auction[name]=price
    value = input("Is there any other bidder, type 'yes' to continue! To exit type 'no'.").lower()
    os.system('cls')
    if value=='yes':
        to_continue = True
    elif value=='no':
        to_continue = False
    else:
        print("This value is not acceptable.")

print(auction)
highest_bid(auction)


