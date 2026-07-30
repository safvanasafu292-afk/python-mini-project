import random 
def get_computer_choice():
    choice=["rock","paper","scissors"]
    computer_choice = random.choice(choice)
    print("computer choice is:",computer_choice)
    return computer_choice


def get_plyer_choice():
    user_choice=input("enter your choice:")
    return user_choice

def check_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print("draw")
    elif(user_choice == "pepar" and computer_choice == "scissors") or (user_choice == "rock" and computer_choice =="pepar")or(user_choice == "scissor" and  computer_choice == "rock"):
        print("computer is winner")
    else:
        print("user winner")

def play_game():
    while True:
       computer=get_computer_choice()
       user_choice=get_plyer_choice()
       check_winner(computer,user_choice)
       break
play_game()



