import random
from hangman_art import stages
from hangman_words import word_list

# Pick a random word from your list of words in the hangman_words module
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the hangman logo from the hangman_art module
from hangman_art import logo
print(logo)

# This tells you the chosen word that was selected. Comment it out to play the guessing game, leave it if you need it to test a feature of your code
# print(f'Pssst, the solution is {chosen_word}.')

# Create a blank list to house the letters that'll make up the word
display = []
# for every character that should be in the word, represent it with _
for _ in range(word_length):
    display += "_"

#   while the game has not ended, execute this conditions
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've guessed {guess} already")

    # for each position that'll house a character, put a letter from the chosen word, if that letter is the same as the guess given
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    # Check if the user gave a guess that's not in the chosen word.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} not in chosen_word. You lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if the user has correctly guessed all letters. If they have, end the game.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])



