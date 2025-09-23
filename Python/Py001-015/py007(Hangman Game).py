# Hamgman Game

import random

logo = (''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')

print(logo)

stages = ['''
   +-----+
   |     |
  (")    |
  /|\    |
 / | \   |
   |     |
  / \    |
 /   \   |
         |
         |
===========
''','''
   +-----+
   |     |
  (")    |
  /|\    |
 / | \   |
   |     |
  /      |
 /       |
         |
         |
===========
''','''
   +-----+
   |     |
  (")    |
  /|\    |
 / | \   |
   |     |
         |
         |
         |
         |
===========
''','''
   +-----+
   |     |
  (")    |
  /|     |
 / |     |
   |     |
         |
         |
         |
         |
===========
''','''
   +-----+
   |     |
  (")    |
   |     |
   |     |
   |     |
         |
         |
         |
         |
===========
''','''
   +-----+
   |     |
  (")    |
         |
         |
         |
         |
         |
         |
         |
===========
''','''
   +-----+
   |     |
         |
         |
         |
         |
         |
         |
         |
         |
===========
''']


word_list = ["ayodhya", "kailash", "warrior", "north", "east", "west", "south", "lanka"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"***************{lives} LIVES LEFT***************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You'vs already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)
    
    if guess not in chosen_word:
        lives -=1
        print(f"You have guessed {guess}, thats not in the word, You lose a life!")

        if lives == 0:
            game_over = True
            print(f"****************It was {chosen_word}, YOU LOSE!****************")

    if "_ " not in display:
        game_over = True
        print("****************You Win!****************")

    print(stages[lives])