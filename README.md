
1. **Clone the repository**:

   ```bash
   git clone https://github.com/CharlesKaleci/Hangman.git
   ```

2. **Navigate into the project directory**:

   ```bash
   cd Hangman
   ```

3. **Ensure you have Python installed** (Python 3.6 or later is recommended).

4. **Install any required packages** (if any additional packages are used, list them here. For this project, no extra packages are required).

## How to Play

1. **Start the Game**:
   Run the following command to start the game:

   ```bash
   python hangman.py
   ```

2. **Gameplay**:
   - The game will display the hangman model and the word to be guessed.
   - Enter a letter to guess. If the letter is in the word, it will be revealed; otherwise, a part of the hangman will be drawn.
   - You can quit the game at any time by entering `q`, and you will be asked to confirm your decision.
   - You have up to 7 incorrect guesses before the game ends.

3. **Winning and Losing**:
   - Guess all the letters in the word before making 7 incorrect guesses to win.
   - If you exceed 7 incorrect guesses, the game will end, and the word will be revealed.

## Code Explanation

Here's a brief overview of the code components:

- **`Hangman` Class**: Main class for the game.
  - **`__init__(self, word_list)`**: Initializes the game settings and selects a random word.
  - **`_initialize_model(self)`**: Sets up the initial hangman model.
  - **`display_model(self)`**: Displays the current hangman model.
  - **`display_word(self)`**: Shows the guessed letters and remaining letters in the word.
  - **`clear_screen(self)`**: Clears the terminal screen for a cleaner display.
  - **`get_user_input(self)`**: Collects and validates user input.
  - **`update_model(self)`**: Updates the hangman model based on the score.
  - **`guess_letter(self, letter)`**: Processes the guessed letter and updates the game state.
  - **`play(self)`**: Main game loop that handles game flow.

- **`words.txt`**: Contains a list of words to be used in the game. Ensure that this file is in the same directory as `hangman.py`.

## Contributing

Feel free to fork the repository and submit pull requests if you have improvements or bug fixes. Please ensure that your code follows the existing style and includes appropriate tests and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
