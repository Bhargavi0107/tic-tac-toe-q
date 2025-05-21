# Tic Tac Toe Game

A complete GUI-based Tic Tac Toe game implemented in Python using Tkinter.

## Features

- Graphical 3x3 game board with intuitive interface
- Two game modes: Human vs Human or Human vs Computer
- Three difficulty levels for computer opponent: Easy, Medium, and Hard
- Clear visual indication of X and O markers
- Visual highlighting of winning combinations
- Status display showing current player's turn and game results
- Score tracking across multiple games
- Reset button to start a new game
- Reset scores functionality
- Error handling for invalid moves

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the directory containing the game files
3. Run the game using:

```bash
python tic_tac_toe.py
```

Or make the file executable and run directly:

```bash
chmod +x tic_tac_toe.py
./tic_tac_toe.py
```

## Game Controls

- **Game Mode**: Choose between "Human vs Human" or "Human vs Computer"
- **Difficulty**: When playing against the computer, select Easy, Medium, or Hard
- **New Game**: Reset the board to start a new game (keeps scores)
- **Reset Scores**: Reset all scores to zero

## Computer AI Levels

- **Easy**: Makes completely random moves
- **Medium**: 50% chance of making a strategic move, 50% random
- **Hard**: Always makes the best strategic move available

## Game Rules

- X always goes first
- Players take turns placing their marker (X or O) on an empty cell
- The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins
- If all cells are filled and no player has won, the game ends in a tie
