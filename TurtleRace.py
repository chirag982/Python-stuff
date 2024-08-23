from turtle import Turtle, Screen,TK
import random

colors = ["red", "orange", "blue", "purple", "green"]
turtles = [""]*5
position = [-60, -30, 0, 30, 60]

def userBet():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race out of these five turtles \nred \norange \nblue \npurple \ngreen")
    
    if user_bet == "":
        userBet()
    if user_bet in colors != True:
        userBet()
    else:
        GameOn(user_bet)


def GameOn(user_bet):
    for i in range(5):
        turtles[i] = Turtle(shape="turtle")
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(-240, position[i])
        turtles[i].pendown()


    is_race_on = True

    while is_race_on:
        r1 = random.randint(0, 10)
        r2 = random.randint(0, 10)
        r3 = random.randint(0, 10)
        r4 = random.randint(0, 10)
        r5 = random.randint(0, 10)

        random_move = [r1, r2, r3, r4, r5]

        for j in range(5):
            turtles[j].forward(random_move[j])
            if turtles[j].xcor() >= 220:
                win = j
                is_race_on = False

    if colors[win] == user_bet:
        print("You won!")
        TK.messagebox.showinfo(title="Result is Out", message="You Won!")
    else:
        TK.messagebox.showinfo(title="Result is Out", message=f"You loose! {colors[win]} turtle win.")

    
screen = Screen()
screen.setup(500, 400)

userBet()
    
screen.exitonclick()
