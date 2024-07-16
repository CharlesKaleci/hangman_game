import random
import os
import time

class Hangman:
    def __init__(self, word_list):
        # Initialize game control flag
        self.control = True
        # Number of rows in the hangman model
        self.rows = 8
        # Player's score (number of wrong guesses)
        self.score = 0
        # Randomly select a word from the provided word list
        self.word = random.choice(word_list).strip()
        # Initialize the list of correct guesses with underscores
        self.correct_guesses = ["_" for _ in self.word]
        # Initialize the hangman model
        self.model = self._initialize_model()
        # Initialize the list of guessed letters
        self.guessed_letters = []

    def _initialize_model(self):
        # Create the initial state of the hangman model
        return [[" " for _ in range(5)] if j == 0 else
                ["-" if _ < 4 else " " for _ in range(5)] if j == 1 else
                [" " for _ in range(5)] if j == 7 else
                ["|" if i == 0 else " " for i in range(5)] for j in range(self.rows)]

    def display_model(self):
        # Display the current state of the hangman model
        for row in self.model:
            print(" ".join(row))
        # Display the guessed letters above the hangman model
        print("\nGuessed letters: " + " ".join(self.guessed_letters))

    def display_word(self):
        # Display the current state of the guessed word
        print(" ".join(self.correct_guesses))

    def clear_screen(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self):
        # Get a letter guess from the user
        user_input = input("\n\nEnter a letter (q to quit): ").lower()
        if user_input == "q":
            # Confirm exit if the user inputs 'q'
            confirm = input("Are you sure you want to quit? (y/n): ").lower()
            if confirm == "y":
                self.control = False
            return None
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter a valid letter!")
            return None
        if user_input in self.guessed_letters:
            print("You have already guessed this letter!")
            return None
        # Add the guessed letter to the list of guessed letters
        self.guessed_letters.append(user_input)
        return user_input

    def update_model(self):
        # Update the hangman model based on the score
        match self.score:
            case 1:
                self.model[2][3] = "O"
            case 2:
                self.model[3][3] = "|"
            case 3:
                self.model[3][2] = "/"
            case 4:
                self.model[3][4] = "\\"
            case 5:
                self.model[4][3] = "|"
            case 6:
                self.model[5][2] = "/"
            case 7:
                self.model[5][4] = "\\"

    def guess_letter(self, letter):
        # Check if the guessed letter is in the word
        if letter in self.word:
            for index, char in enumerate(self.word):
                if char == letter:
                    self.correct_guesses[index] = letter
        else:
            print("This letter is not in the word.")
            self.score += 1
            self.update_model()
            time.sleep(1)  # Wait for 1 second after a wrong guess

    def play(self):
        # Main game loop
        while self.score <= 7 and "_" in self.correct_guesses and self.control:
            self.clear_screen()
            self.display_model()
            self.display_word()
            user_input = self.get_user_input()
            if user_input:
                self.guess_letter(user_input)

        self.clear_screen()
        if "_" not in self.correct_guesses:
            print(f"Congratulations! You correctly guessed the word: {self.word}")
        else:
            if self.control:
                print(f"Sorry, you lost. The word was: {self.word}")
            else:
                print(f"You quit the game. The word was: {self.word}")
            time.sleep(2)  # Wait for 2 seconds before ending the game


# Read words from the file
with open("words.txt", "r") as file:
    words = file.readlines()

# Check if words list is empty
if not words:
    print("Word list is empty. Please add words to the list.")
else:
    # Start the game
    hangman_game = Hangman(words)
    hangman_game.play()
