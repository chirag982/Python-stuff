import random
import pyfiglet
ASCII_art_1 = pyfiglet.figlet_format("Hangman")

word_list = ["ardvark", "baboon", "camel"]
print("Welcome to the game Hangman.")
print(ASCII_art_1)

chosen_word = random.choice(word_list)
chosen_length = int(len(chosen_word))

display = []
        
for letter in chosen_word:
    display += "_"
print(display)

guess=[0]*7
hang=0
for j in range(0,26):    
    
    guess[j] = input("Guess a letter: ").lower()

    boolean = True
    for i in range(0,chosen_length):
        if chosen_word[i] == guess[j]:
            display[i]=guess[j]
            boolean = False

    if boolean == False:
        print("Correct guess!")    
    if boolean == True:
        hang = hang + 1
        print("Sorry, but wrong answer!")

    if hang==0:
        print("------- ")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-")
        
    if hang==1:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|")
        print("|")
        print("|")
        print("-")
        
    if hang==2:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|      |")
        print("|")
        print("|")
        print("-")
        
    if hang==3:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|     /|")
        print("|")
        print("|")
        print("-")
        
    if hang==4:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|     /|\\")
        print("|")
        print("|")
        print("-")
        
    if hang==5:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|     /|\\")
        print("|     /")
        print("|")
        print("-")

    if hang==6:
        print("------- ")
        print("|      |")
        print("|      0")
        print("|     /|\\")
        print("|     / \\")
        print("|")
        print("-")
        print("Hangman dead now. Game Over!")
        exit()
            
    print(display)
    
    count = 0
    for word in display:
        if word == "_":
            count += 1
    if count==0:
        print("Game Over, you win!")
        exit()
                
print("Game Over, You lost!")
        





        

