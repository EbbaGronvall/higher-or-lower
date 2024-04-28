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
    difficulties = {
        "easy": 10,
        "medium": 15,
        "hard": 20,
    }
    print("Choose difficulty (easy, medium, hard): ")
    while True:
        difficulty = input("Enter your choice: ").lower()
        if difficulty in difficulties:
            return difficulty, difficulties[difficulty]
        else:
            print("Invalid difficulty! Please choose between easy, medium or hard!")
    

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
        print("Invalid number of sounds. Please choose 3, 5 or 10.")
        rounds = input("Choose the number of rounds (3, 5 or 10): ")
    return int(rounds)            



welcome_message() 
difficulty = choose_difficulty()
rounds = choose_rounds()   
secret_number = generate_number(difficulty)
run_game(difficulty, rounds, secret_number)