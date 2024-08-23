import random

def print_display(dealer, dealer_draw, user, user_draw, dealer_cards, user_cards):
    print(" ")
    print("Dealer Cards are: ")
    for i in range(0,len(dealer_cards)):
        print(dealer_cards[i])
    print(f"dealer score = {dealer}")
    print("vs")
    print("User Cards are: ")
    for j in range(0,len(user_cards)):
        print(user_cards[j],"\t")
    print(f"User score = {user}")
    print(" ")

def check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards):
    if again=='w':
        if dealer==dealer2:
            dealer=dealer1+dealer2
            check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)
        if dealer == 21:
            print(f"You loose! your score={user} and dealer={dealer}, dealer wins!")
            exit()
        if dealer > 21:
            print(f"You Win! your score={user} and dealer={dealer}.")
            exit()
        if dealer < 17:
            again = 'w'
            dealer3 = random.choice(cards)
            dealer = dealer + dealer3
            dealer_draw += 1
            dealer_cards.append(dealer3)
            #print function called
            print_display(dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)        
            # Recalling that function
            check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)
        else:
            if dealer > user:
                print(f"You loose! your score={user} and dealer={dealer}, dealer wins!")
                exit()
            elif user > dealer:
                print(f"You Win! your score={user} and dealer={dealer}.")
                exit()
            elif user == dealer:
                if user_draw>dealer_draw:
                    print(f"You loose! your score={user} and dealer={dealer}, dealer wins!")
                    exit()
                elif dealer_draw>user_draw:
                    print(f"You Win! your score={user} and dealer={dealer}.")
                    exit()
                else:
                    print("Match Draw!")
                    exit()
    if again=='d':
        user3 = random.choice(cards)
        user += user3
        user_draw = user_draw +1
        user_cards.append(user3)
        #print function called
        print_display(dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)        
        if user==21:
            print(f"You Win! your score={user} and dealer={dealer}.")
            exit()
        if user>21:
            print(f"You loose! your score={user} and dealer={dealer}, dealer wins!")
        else:
            again = input("Type 'w' to wait or type 'd' to draw another.").lower()
            # Recalling that function
            check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)
    else:
        print("Sorry, this value can't be processed. Go again...")
        again = input("Type 'w' to wait or type 'd' to draw another.").lower()
        # Recalling that function
        check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)




cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
print("Welcome to the blackjack!")

dealer = 0
user = 0
dealer_draw=0
user_draw=0

# On start give two cards each to dealer and user

# dealer starting cards
dealer1=random.choice(cards)
dealer2=random.choice(cards)
dealer_draw = 2
dealer = dealer2

# user starting cards
user1=random.choice(cards)
user2=random.choice(cards)
user_draw = 2
user = user1+user2

print(" ")
print(f"Dealer : [?],{dealer2}  Score:{dealer}")
print("vs")
print(f"Your : {user1}, {user2}  Score:{user}")
print(" ")

dealer_cards = ['[?]', dealer2]
user_cards = [user1, user2]

# If in first step only user wins i.e. 21 results by the sum 
if user==21:
    print("blackjack!")
    print("You Win!")

again = input("Type 'w' to wait or type 'd' to draw another.").lower()
if again=='w':
    if dealer==dealer2:
        dealer=dealer1+dealer2
#Calling the function check....
check(again, dealer, dealer_draw, user, user_draw, dealer_cards, user_cards)
print("Game Over!")


