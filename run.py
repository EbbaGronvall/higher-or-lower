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
    instructions = """
    In this game you are guessing which random number the computer have.
    To start with you have to choose the difficulty.
    There is easy(numbers 1-10), medium(numbers 1-15) and hard(numbers 1-20).
    Then you will be asked to choose how many rounds you wanna go. 3, 5 or 10.
    Say you pick easy and 3 rounds.
    You will be asked to say a number between 1 and 10.
    If it is correct the computer will tell you so.
    If not the computer will tell you if the number is higher or lower.
    You have 3 attempts to get it right otherwise the computer wins the round.
    So lets get started!
    """
    print(instructions)


def get_name():
    """
    The user is asked to put in their name for personalization
    """
    while True:
        try:
            user_name = input("First please enter your name:\n").capitalize()
            if not user_name.isalpha():
                raise ValueError(Fore.RED + "Invalid input! Please enter your"
                                          + " name using letters only.")
            print(f"Let's go {user_name}!\n")
            break
        except ValueError:
            print(Fore.RED + f"Invalid input! Please enter your name using"
                           + " letters only.")
    return user_name


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
        difficulty = input("Choose the difficulty:\n").lower()
        if difficulty in difficulties:
            return difficulty, difficulties[difficulty]
        else:
            print(Fore.RED + "Invalid difficulty! Please choose between easy,"
                           + " medium or hard!")


def choose_rounds():
    """
    The user chooses number of rounds they want to play
    """
    rounds = input("Choose the number of rounds (3, 5 or 10):\n")
    while rounds not in ["3", "5", "10"]:
        print(Fore.RED + "Invalid number of rounds. Please choose 3, 5 or 10.")
        rounds = input("Choose the number of rounds (3, 5 or 10): ")
    return int(rounds)


def generate_number(difficulty_upper_bound):
    """
    Generates numbers depending on the difficulty
    """
    return random.randint(1, difficulty_upper_bound)


def run_game(difficulty_upper_bound, rounds, secret_number, user_name):
    """
    A function that runs the game once difficulty and rounds are chosen
    """
    user_score = 0
    computer_score = 0
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        secret_number = generate_number(difficulty_upper_bound)
        print("The computer has picked a number.")
        guess = None
        attempts = 0
        while attempts < 3:
            guess, attempts = check_answer(guess, secret_number, attempts,
                                           user_name)
            if guess == secret_number:
                user_score += 1
                break
        if guess != secret_number:
            print(Fore.RED + f"Sorry {user_name}, you didn't guess the correct"
                           + f" number. The correct number is {secret_number}")
            computer_score += 1
    final_score(user_score, computer_score, user_name)


def check_answer(guess, secret_number, attempts, user_name):
    """
    Checks to see if guess == secret_number
    """
    try:
        guess = int(input(f"Enter your guess:\n"))
        if guess < 1 or guess > difficulty_upper_bound:
            print(Fore.RED + f"Invalid guess! Please enter a number between"
                           + f" 1 and {difficulty_upper_bound}.")
        else:
            if guess < secret_number:
                print("Higher!")
                attempts += 1
            elif guess > secret_number:
                print("Lower!")
                attempts += 1
            else:
                print(Fore.GREEN + f"Congratulations {user_name}! You guessed"
                                 + f" the correct number ({secret_number}) in"
                                 + f" {attempts + 1} attempts.")
                attempts += 1
    except ValueError:
        print(Fore.RED + f"Invalid input! Please enter a valid number.")
    return guess, attempts


def final_score(user_score, computer_score, user_name):
    """
    Checks to see if the user won or lost
    """
    if user_score == computer_score:
        print(f.renderText("IT'S A TIE!"))
        print(f"You and the computer tied for first place with {user_score} to"
              + f" {computer_score}!")
    elif computer_score == user_score + 1:
        print(Fore.RED + f.renderText("SO CLOSE"))
        print(f"That was so close {user_name}! You lost by only 1 point..")
        print(f"The final score is {user_score} to {computer_score}..")
    elif user_score == computer_score + 1:
        print(Fore.GREEN + f.renderText("A WIN IS A WIN"))
        print(f"Wow {user_name} you won by just 1 point!")
        print(f"The final score is {user_score} to {computer_score}.")
    elif user_score < computer_score:
        print(Fore.RED + f.renderText("GAME OVER!"))
        print(f"Sorry {user_name}.. You lost by {user_score} to"
              + f" {computer_score}..")
    else:
        print(Fore.GREEN + f.renderText("YOU WON!"))
        print(f"Great job {user_name}! You won by {user_score} to"
              + f" {computer_score}!")


if __name__ == "__main__":
    welcome_message()
    user_name = get_name()
    difficulty_name, difficulty_upper_bound = choose_difficulty()
    rounds = choose_rounds()
    secret_number = generate_number(difficulty_upper_bound)
    run_game(difficulty_upper_bound, rounds, secret_number, user_name)
