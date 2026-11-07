# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game for two players, written in Python.

## Requirements

- Python 3
- No external packages are needed

## How to play

1. Run the program.
2. Players take turns. Player **X** goes first, followed by player **O**.
3. Enter a number from **1** to **9** to choose a square on the board:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

4. The game announces a winner when a player completes a row, column, or diagonal. If all nine squares are filled without a winner, the game ends in a draw.

## Run the game

Save the Python code as `tic_tac_toe.py`, open a terminal in the same folder, and run:

```bash
python3 tic_tac_toe.py
```

In a Jupyter notebook, paste the code into a code cell and run that cell instead.

## Input handling

The program checks that each move is a number from 1 to 9 and that the chosen square is not already occupied. It asks the player to choose again if the input is invalid.
