import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")

        winner = get_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!\n")
        elif winner == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
