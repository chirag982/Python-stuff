import random

def Number_guess(number, level_chosen):
    user = 0
    if level_chosen == 'hard':
        for i in range(0,5):
            print(f"You have only {5-i} guesses to guess the number.")
            user = int(input("Make your guess : "))
            if user > number:
                print("Too high!")
            elif user == number:
                print("You Guessed it right, you win!")
                exit()
            else:
                print("Too low!")
        print("You lost!")
        exit()
        
            
    elif level_chosen == 'easy':
        for j in range(0,10):
            print(f"You have only {10-j} attempts remaining to guess the number.")
            user = int(input("Make your guess : "))
            if user > number:
                print("Too high!")
            elif user == number:
                print("You Guessed it right, you win!")
                exit()
            else:
                print("Too low!")
        print("You lost!")
        exit()
        
    else:
        print("Not acceptable! Go again.")
        level = input("What level you want to choose 'Hard' or 'Easy'.").lower()
        Number_guess(number, level)
        

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
# Generated a random number
a = random.randint(1,100)
# Level decided
level = input("What level you want to choose 'Hard' or 'Easy'.").lower()
# Calling of the function
Number_guess(a, level)


