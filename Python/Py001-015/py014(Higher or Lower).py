# Higher or Lower

# Art
logo = ('''
  _   _ ___ ____ _   _ _____ ____  
 | | | |_ _/ ___| | | | ____|  _ \ 
 | |_| || | |  _| |_| |  _| | |_) |
 |  _  || | |_| |  _  | |___|  _ < 
 |_| |_|___\____|_| |_|_____|_| \_\_
                                   
  _     _____        _______ ____  
 | |   / _ \ \      / / ____|  _ \ 
 | |  | | | \ \ /\ / /|  _| | |_) |
 | |__| |_| |\ V  V / | |___|  _ < 
 |_____\___/  \_/\_/  |_____|_| \_\_
                                   
''')

vs = ('''
 __     ______  
 \ \   / / ___| 
  \ \ / /\___ \ 
   \ V /  ___) |
    \_/  |____/ 
''')


# Game Data
data = [
    {
        'name' : 'Karan Aujla',
        'follower_count' : 11,
        'description' : 'Singer',
        'country' : 'India',
    },
        {
        'name' : 'Talwinder',
        'follower_count' : 2,
        'description' : 'Singer',
        'country' :  'India',
    },
        {
        'name' : 'Amrinder Gill',
        'follower_count' : 3,
        'description' : 'Singer',
        'country' : 'Indian',
    },
        {
        'name' : 'Robert Downey Jr.',
        'follower_count' : 57,
        'description' : 'Actor',
        'country' : 'American',
    },
        {
        'name' : 'Yo Yo Honey Singh',
        'follower_count' : 20,
        'description' : 'Singer',
        'country' : 'Indian',
    },
        {
        'name' : 'Sydney Sweeney',
        'follower_count' : 25,
        'description' : 'Actor',
        'country' : 'American'
    },
        {
        'name' : 'Cristiano Ronaldo',
        'follower_count' : 663,
        'description' : 'Footballer',
        'country' : 'Portuguese'
    },
        {
        'name' : 'Leo Messi',
        'follower_count' : 506,
        'description' : 'Footballer',
        'country' : 'Argentine ',
    }
]

import random

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        if user_guess == "a":
            return user_guess == "a"
        else:
            return user_guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
    # Format the account data into printable format
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, is {account_country}"

while game_should_continue:
    # Generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")


    # Ask the user for a guess
    guess = input("Who has more follower? Typr 'A' or 'B' : ")
    print("\n" * 50)

    # Check if the user is correct

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You're right! Current Score : {score}")
    else:
        print(f"Sorry, that's wrong. Final Score : {score}")
        game_should_continue = False