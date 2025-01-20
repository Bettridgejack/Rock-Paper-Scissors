import random 

def get_computer_decision():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def winner_selection(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Its a tie! \nLets Play Again!"
    elif user_choice == "rock" and computer_choice == "scissors" or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You Win! \nLets Play Again!"
    else:
        return "You Lose! \nLets Play Again!"

while True:
    user_choice = input("Please choose, rock, paper or scissors. (or type 'quit' to leave): ")
    if user_choice == "quit":
        print("Thanks for playing")
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Please enter a valid choice")
        continue

    computer_choice = get_computer_decision()
    print(f"Computer Chose {computer_choice}")
    result = winner_selection(user_choice, computer_choice)
    print(result)

    