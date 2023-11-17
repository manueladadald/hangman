import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo + "\n")
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    
    guess = input("\nGuess a letter: ").lower()
    os.system('cls')
    letters = []
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if guess not in letters:
            if letter == guess:
                display[position] = letter
                
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Oh no! You're out of lifes :( \nThe word was {chosen_word} \nGAME OVER")
    print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You won!")
