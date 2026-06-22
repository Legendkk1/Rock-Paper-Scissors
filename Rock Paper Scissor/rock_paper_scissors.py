import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        player_input = input("Enter your choice rock, paper, or scissors: ").lower()
        if player_input in choices:
            return player_input
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "It's a tie!":
            print("It's a tie!")
        elif result == "You win!":
            print("Congratulations! You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()