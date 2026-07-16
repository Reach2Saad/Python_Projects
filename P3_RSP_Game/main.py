"""Rock-Scissors-Paper game: Player vs Computer."""
import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {ROCK : "🪨", SCISSORS: "✂️", PAPER: "📜"}
choices = tuple(emojis.keys())

def get_user_choice():
    """Prompt and validate player input."""
    while True:
        user_choice = input("\nChoose Rock, Scissor or Paper? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice! please chose correct one.")
            

def display_choices(user_choice, computer_choice):
    """Display player and computer choices with emojis."""
    print(f"You choose {emojis[user_choice]}")
    print(f"Computer choose {emojis[computer_choice]}")


def determine_winner(user_choice,computer_choice):
    """Evaluate round result and display outcome."""
    if user_choice == computer_choice:
        print("Draw! ⚖️")

    elif (
        (user_choice== ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win! 🏆")

    else:
        print("You lost! 😔" )

def ask_to_continue():
    """Prompt player to continue or exit."""
    while True:
        should_continue= input("\nContinue? (y/n): ").lower()
        if should_continue in ["y", "n"]:
            return should_continue 
        else:
            print("invalid choice! please choose correct one. (y/n)")
       
def play_game():
    """Execute main game loop."""
    while True:
        user_choice = get_user_choice()   

        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
        
        continue_game = ask_to_continue()
        if continue_game == 'n':
            print("Thankyou for Playing!")
            break

print("=" * 35)
print("🎮 ROCK PAPER SCISSORS 🪨 📃✂️  🎮")
print("=" * 35)

play_game()
        

    
        