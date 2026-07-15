"""Rock-Scissors-Paper game: Player vs Computer."""
import random

emojis = {"r" : "🪨", "s": "✂️", "p": "📜"}
choices = ("r","s","p")

def get_user_choice():
    """Prompt and validate player input."""
    while True:
        user_choice = input("Choose Rock, Scissor or Paper? (r/p/s): ").lower()
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
        (user_choice== "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or 
        (user_choice == "p" and computer_choice == "r")):
        print("You win! 🏆")

    else:
        print("You lost! 😔" )

def ask_to_continue():
    """Prompt player to continue or exit."""
    while True:
        should_continue= input("Continue? (y/n): ").lower()
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
        

    
        