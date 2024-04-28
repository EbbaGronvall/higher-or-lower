import random
from colorama import Fore, init
from pyfiglet import Figlet
f = Figlet(font='big')
init(autoreset=True)
def welcome_message():
    """
    Welcomes the user to the game and gives the instructions.
    """
    
    print(f.renderText("Welcome to Higher or Lower!"))
    print("In this game you are guessing which random number the computer have.")
    print("To start with you have to choose the difficulty.\nThere is easy(numbers 1-10), medium(numbers 1-15) and hard(numbers 1-20)\n")  
    print("Then you will be asked to choose how many rounds you wanna go. 3, 5 or 10\n") 
    print("Say you pick easy and 3 rounds. You will be asked to say a number between 1 and 10. If it is correct the computer will tell you so. If not the computer will tell you if the number is higher or lower. You have 3 attempts to get it right otherwise the computer wins the round.")
    print("\nSo lets get started!")

 
def choose_difficulty():
    """
    The user chooses the difficulty
    """
    difficulties = {
        "easy": 10,
        "medium": 15,
        "hard": 20,
    }
    while True:
        difficulty = input("Choose the difficulty: ").lower()
        if difficulty in difficulties:
            return difficulty, difficulties[difficulty]
        else:
            print(Fore.RED + "Invalid difficulty! Please choose between easy, medium or hard!")
    

def generate_number(difficulty_upper_bound):
    """
    Generates numbers depending on the difficulty
    """
    return random.randint(1, difficulty_upper_bound)

def choose_rounds():
    """
    The user chooses number of rounds they want to play
    """
    rounds = input("Choose the number of rounds (3, 5 or 10): ")
    while rounds not in ["3", "5", "10"]:
        print(Fore.RED + "Invalid number of rounds. Please choose 3, 5 or 10.")
        rounds = input("Choose the number of rounds (3, 5 or 10): ")
    return int(rounds)            

def run_game(difficulty_name, difficulty_upper_bound, rounds, secret_number):
    """
    A function that runs the game once difficulty and number of rounds are chosen
    """
    user_score = 0
    computer_score = 0 
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        print("The computer has picked a number.")
        guess = None
        attempts = 0
        while attempts < 3:
            try:
                guess = int(input(f"Enter your guess: "))
                if guess < 1 or guess > difficulty_upper_bound:
                    print(Fore.RED + f"Invalid guess! Please enter a number between 1 and {difficulty_upper_bound}.")
                else:
                    if guess < secret_number:
                        print("Higher!")
                    elif guess > secret_number:
                        print("Lower!")
                    else:
                        print(Fore.GREEN + f"Congratulations! You've guessed the correct number ({secret_number}) in {attempts + 1} attempts.") 
                        user_score += 1
                        break
                    attempts += 1
            except ValueError:
                print(Fore.RED + f"Invalid input! Please enter a valid number.")
        if attempts == 3:
            print(Fore.RED + f"Sorry, you didn't guess the correct number. The correct number was {secret_number}") 
            computer_score += 1
    if user_score < computer_score:
        print(Fore.RED + f.renderText("GAME OVER!"))
        print(f"You lost by {user_score} to {computer_score}..")
    else:
        print(Fore.GREEN + f.renderText("YOU WON!"))  
        print(f"You won by {user_score} to {computer_score}!")                               


welcome_message() 
difficulty_name, difficulty_upper_bound = choose_difficulty()
rounds = choose_rounds()   
secret_number = generate_number(difficulty_upper_bound)
run_game(difficulty_name, difficulty_upper_bound, rounds, secret_number)

                              