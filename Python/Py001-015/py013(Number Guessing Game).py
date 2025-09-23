# Number Guessing Game

logo = ('''
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
        ''')

#Choosing a random number between 1 and 100
from random import randint

easy_level_turns = 10
hard_level_turns = 5

turns = 0

#Function to check user's guess againt actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining!"""
    if user_guess > actual_answer:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")


#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
    #Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        #Let the use user guess a number
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, YOU LOSE!")
            return
        elif guess != answer:
            print("Guess Again!")
game()# Number Guessing Game

logo = ('''
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
        ''')

#Choosing a random number between 1 and 100
from random import randint

easy_level_turns = 10
hard_level_turns = 5

turns = 0

#Function to check user's guess againt actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining!"""
    if user_guess > actual_answer:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")


#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
    #Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        #Let the use user guess a number
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, YOU LOSE!")
            return
        elif guess != answer:
            print("Guess Again!")
game()