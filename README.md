**Trivia Quiz Game**

This is a Python-based trivia quiz game that uses the Open Trivia API to generate questions and answers for the player to answer. The game uses a simple graphical user interface (GUI) created with the Tkinter library.

**Installation**
To run the game, you will need to have Python 3 installed on your computer. You can download Python 3 from the official website at https://www.python.org/downloads/.

You will also need to install the requests library, which you can do by running the following command in your terminal or command prompt:

pip install requests

**Usage**

To play the game, simply run the main.py file in your Python environment:

python main.py

The game will start, and you will be presented with a series of multiple-choice questions. Use the buttons to select your answer, and the game will keep track of your score.

**Files**

This project consists of the following files:

data.py: Contains the code that retrieves the question data from the Open Trivia API.
main.py: Contains the main code for the game, including the game loop and the user interface.
question_model.py: Contains the Question class, which is used to represent each question in the game.
quiz_brain.py: Contains the QuizBrain class, which manages the game state and checks the player's answers.
ui.py: Contains the QuizInterface class, which creates the graphical user interface for the game.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
This project was created as part of a Python course on Udemy, and was inspired by the Trivia API project on the FreeCodeCamp website.