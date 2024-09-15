# Kuireimung-Identification-of-player-with-Highest-total-score-across-matches

# OrangeCap: Identify the Player with the Highest Total Score
## Introduction
The `OrangeCap` project is a simple Python script designed to process the scores of multiple
players across several matches and determine the player with the highest total score. This
concept is inspired by the "Orange Cap" in cricket, which is awarded to the highest run-scorer
in a tournament. The script uses a dictionary to store the scores of players in di erent
matches and then calculates the cumulative score for each player. The player with the
highest total score is then identifi ed and displayed.
## Project Overview
This project includes a Python function `orangecap` that takes in a dictionary containing
match scores and returns the player with the highest aggregate score. The dictionary is
structured such that each key represents a match, and each value is another dictionary
containing player names as keys and their respective scores as values
.
### Key Features
```
python
scores_dict = {
'match1': {'player1': 57, 'player2': 38},
'match2': {'player3': 9, 'player1': 42},
'match3': {'player2': 41, 'player4': 63, 'player3': 91}
}
- **
Score Aggregation**: The function calculates the total score for each player across
multiple matches.
- **Highest Scorer Identifi cation**: It identifi es the player with the highest total score.
- **Simple and Reusable**: The function is designed to be easily integrated into larger
projects or used on its own.
## Installation
There is no installation required for this project. You only need Python installed on your
machine to run the script. If you don’t have Python installed, you can download it from
[python.org](https://www.python.org/downloads/)
.
### Requirements
- Python 3.x
## Usage
Here is an example of how to use the `orangecap` function:
### Example Input
The input to the function is a dictionary that contains match data. Each match is represented
as a key, and the value is another dictionary with player names and their respective scores
.
