import random
def welcome_message():
    """
    Welcomes the user to the game and gives the instructions.
    """
    print("Welcome to Higher or Lower!\nIn this game you are guessing which random number the computer have.\n")
    print("To start with you have to choose the difficulty.\nThere is easy(numbers 1-10), medium(numbers 1-15) and hard(numbers 1-20)\n")  
    print("Then you will be asked to choose how many rounds you wanna go. 3, 5 or 10\n") 
    print("Say you pick easy and 3 rounds. You will be asked to say a number between 1 and 10. If it is correct the computer will tell you so. If not the computer will tell you if the number is higher or lower. If you get it right this time you win the round, if not the computer wins the round.")
    print("\nSo lets get started!")

 
def choose_difficulty():
    """
    The user chooses the difficulty
    """
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty, please choose between easy, medium or hard!")
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    return difficulty

def generate_number(difficulty):
    """
    Generates numbers depending on the difficulty
    """
    if difficulty == "easy":
        return random.randint(1, 10)
    elif difficulty == "medium":
        return random.randint(1, 15)
    elif difficulty == "hard":
        return random.randint(1, 20)

def choose_rounds():
    """
    The user chooses number of rounds they want to play
    """
    rounds = input("Choose the number of rounds (3, 5 or 10): ")
    while rounds not in ["3", "5", "10"]:
        print("Invalid number of sounds. Please choose 3, 5 or 10.")
        rounds = input("Choose the number of rounds (3, 5 or 10): ")
    return int(rounds)            

def run_game(difficulty, rounds):
    """
    A function that runs the game once difficulty and number of rounds are chosen
    """
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        secret_number = generate_number(difficulty)
        print("The computer has picked a number.")
        guess = None
        attempts = 0 
        while attempts < 2:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Higher!")
            elif guess > secret_number:
                print("Lower!")
            else:
                print(f"Congratulations! You've guessed the correct number({secret_number}) in {attempts} attempts.")
                break
        if attempts == 2:
            print(f"Sorry, you didn't guess the correct number. The correct number was {secret_number}.")

welcome_message() 
difficulty = choose_difficulty()
rounds = choose_rounds()   
generate_number(difficulty)
run_game(difficulty, rounds)