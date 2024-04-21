import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    play_again = True
    user_score = 0
    computer_score = 0

    while play_again:
        play_game()

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        while play_again_input not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again_input = input("Do you want to play again? (yes/no): ").lower()

        if play_again_input == 'no':
            play_again = False

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
