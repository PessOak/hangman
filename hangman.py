import random
from words import words
import string
import time
from hang_visual import hang_visual_dict

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)  #letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #what was guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) -> 'a b cd'
        #time.sleep(1)
        print("You have ", lives, " lives left and you have used these letters: ", " ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        time.sleep(0.5)
        print(hang_visual_dict[lives])
        time.sleep(0.5)
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                time.sleep(0.5)
                print("Letter is not in word.")
        
        elif user_letter in used_letters:
            time.sleep(0.5)
            print("You have already used that character")
        
        else:
            time.sleep(0.5)
            print("Invalid character. Try again")

    #gets here when lives = 0 or len(word) = 0
    time.sleep(0.5)
    if lives == 0:
        print(hang_visual_dict[lives])
        print("You died, sorry. The word was ", word)
    else: 
        print("You won! You guessed the word ", word, " correctly!!")

hangman()
