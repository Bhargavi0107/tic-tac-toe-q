#!/usr/bin/env python3
"""
Tic Tac Toe Game with GUI
-------------------------
A complete implementation of Tic Tac Toe with a graphical interface using Tkinter.
Features:
- Human vs Human or Human vs Computer gameplay
- Multiple difficulty levels for computer opponent
- Score tracking across games
- Visual indication of winning combinations
- Game status display
- Reset functionality
"""

import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class TicTacToe:
    def __init__(self, root):
        """Initialize the Tic Tac Toe game with GUI elements"""
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.current_player = "X"  # X always starts
        self.board = [""] * 9  # 3x3 board represented as a list
        self.game_active = True
        self.game_mode = "human_vs_human"  # Default mode
        self.difficulty = "medium"  # Default difficulty
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        
        # Create frames
        self.create_frames()
        
        # Create game controls
        self.create_controls()
        
        # Create the game board
        self.create_board()
        
        # Create status display
        self.create_status_display()
        
        # Create score display
        self.create_score_display()
        
        # Update the status display
        self.update_status()

    def create_frames(self):
        """Create the main frames for the game layout"""
        # Top frame for game controls
        self.control_frame = tk.Frame(self.root, bg="#f0f0f0", padx=10, pady=10)
        self.control_frame.pack(fill="x")
        
        # Middle frame for the game board
        self.board_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.board_frame.pack()
        
        # Bottom frame for status and score
        self.status_frame = tk.Frame(self.root, bg="#f0f0f0", padx=10, pady=10)
        self.status_frame.pack(fill="x")

    def create_controls(self):
        """Create game control elements"""
        # Game mode selection
        tk.Label(self.control_frame, text="Game Mode:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.mode_var = tk.StringVar(value="human_vs_human")
        mode_menu = ttk.Combobox(self.control_frame, textvariable=self.mode_var, 
                                 values=["Human vs Human", "Human vs Computer"],
                                 state="readonly", width=15)
        mode_menu.grid(row=0, column=1, padx=5, pady=5)
        mode_menu.bind("<<ComboboxSelected>>", self.change_game_mode)
        
        # Difficulty selection (initially disabled)
        tk.Label(self.control_frame, text="Difficulty:", bg="#f0f0f0").grid(row=0, column=2, padx=5, pady=5)
        self.difficulty_var = tk.StringVar(value="Medium")
        self.difficulty_menu = ttk.Combobox(self.control_frame, textvariable=self.difficulty_var,
                                           values=["Easy", "Medium", "Hard"],
                                           state="disabled", width=10)
        self.difficulty_menu.grid(row=0, column=3, padx=5, pady=5)
        self.difficulty_menu.bind("<<ComboboxSelected>>", self.change_difficulty)
        
        # Reset button
        self.reset_button = tk.Button(self.control_frame, text="New Game", 
                                     command=self.reset_game, bg="#4CAF50", fg="white",
                                     activebackground="#45a049", width=10)
        self.reset_button.grid(row=0, column=4, padx=10, pady=5)
        
        # Reset scores button
        self.reset_scores_button = tk.Button(self.control_frame, text="Reset Scores", 
                                           command=self.reset_scores, bg="#f44336", fg="white",
                                           activebackground="#d32f2f", width=10)
        self.reset_scores_button.grid(row=0, column=5, padx=10, pady=5)

    def create_board(self):
        """Create the 3x3 game board with buttons"""
        self.cells = []
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                cell = tk.Button(self.board_frame, text="", font=("Arial", 24, "bold"),
                               width=3, height=1, bg="#ffffff",
                               command=lambda idx=index: self.make_move(idx))
                cell.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                self.cells.append(cell)
                
        # Configure grid to expand cells
        for i in range(3):
            self.board_frame.grid_rowconfigure(i, weight=1)
            self.board_frame.grid_columnconfigure(i, weight=1)

    def create_status_display(self):
        """Create the status display showing game state"""
        self.status_label = tk.Label(self.status_frame, text="", font=("Arial", 12),
                                   bg="#f0f0f0", pady=5)
        self.status_label.pack(side="top", fill="x")

    def create_score_display(self):
        """Create the score display"""
        score_frame = tk.Frame(self.status_frame, bg="#f0f0f0")
        score_frame.pack(side="top", fill="x", pady=5)
        
        # X score
        self.x_score_var = tk.StringVar(value="X: 0")
        x_label = tk.Label(score_frame, textvariable=self.x_score_var, 
                         font=("Arial", 12), bg="#e6f7ff", width=8)
        x_label.pack(side="left", padx=10)
        
        # Tie score
        self.tie_score_var = tk.StringVar(value="Ties: 0")
        tie_label = tk.Label(score_frame, textvariable=self.tie_score_var, 
                           font=("Arial", 12), bg="#f5f5f5", width=8)
        tie_label.pack(side="left", padx=10)
        
        # O score
        self.o_score_var = tk.StringVar(value="O: 0")
        o_label = tk.Label(score_frame, textvariable=self.o_score_var, 
                         font=("Arial", 12), bg="#ffe6e6", width=8)
        o_label.pack(side="left", padx=10)

    def update_status(self):
        """Update the status display with current game state"""
        if not self.game_active:
            return
            
        if self.game_mode == "human_vs_computer" and self.current_player == "O":
            self.status_label.config(text=f"Computer's turn (O)")
        else:
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def update_scores(self):
        """Update the score display"""
        self.x_score_var.set(f"X: {self.scores['X']}")
        self.o_score_var.set(f"O: {self.scores['O']}")
        self.tie_score_var.set(f"Ties: {self.scores['Tie']}")

    def make_move(self, index):
        """Handle a player's move on the board"""
        # Check if the cell is empty and the game is active
        if self.board[index] == "" and self.game_active:
            # Update the board and UI
            self.board[index] = self.current_player
            self.cells[index].config(text=self.current_player, 
                                   bg="#e6f7ff" if self.current_player == "X" else "#ffe6e6")
            
            # Check for win or tie
            if self.check_winner():
                self.game_active = False
                self.scores[self.current_player] += 1
                self.update_scores()
                self.status_label.config(text=f"Player {self.current_player} wins!")
            elif "" not in self.board:  # Check for tie
                self.game_active = False
                self.scores["Tie"] += 1
                self.update_scores()
                self.status_label.config(text="Game ended in a tie!")
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_status()
                
                # If playing against computer and it's computer's turn
                if self.game_active and self.game_mode == "human_vs_computer" and self.current_player == "O":
                    self.root.after(500, self.computer_move)  # Delay for better UX

    def computer_move(self):
        """Handle the computer's move based on difficulty level"""
        if not self.game_active:
            return
            
        # Different AI strategies based on difficulty
        if self.difficulty == "easy":
            self.make_random_move()
        elif self.difficulty == "medium":
            # 50% chance of making a smart move, 50% random
            if random.random() < 0.5:
                self.make_smart_move()
            else:
                self.make_random_move()
        else:  # Hard difficulty
            self.make_smart_move()

    def make_random_move(self):
        """Make a random valid move for the computer"""
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
        if empty_cells:
            move = random.choice(empty_cells)
            self.make_move(move)

    def make_smart_move(self):
        """Make a strategic move for the computer"""
        # Check if computer can win in the next move
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"  # Try placing O
                if self.check_winner(highlight=False):
                    self.board[i] = ""  # Reset for actual move
                    self.make_move(i)
                    return
                self.board[i] = ""  # Reset after checking
        
        # Check if player can win in the next move and block
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"  # Try placing X
                if self.check_winner(highlight=False):
                    self.board[i] = ""  # Reset for actual move
                    self.make_move(i)
                    return
                self.board[i] = ""  # Reset after checking
        
        # Take center if available
        if self.board[4] == "":
            self.make_move(4)
            return
            
        # Take corners if available
        corners = [0, 2, 6, 8]
        empty_corners = [i for i in corners if self.board[i] == ""]
        if empty_corners:
            self.make_move(random.choice(empty_corners))
            return
            
        # Take any available edge
        edges = [1, 3, 5, 7]
        empty_edges = [i for i in edges if self.board[i] == ""]
        if empty_edges:
            self.make_move(random.choice(empty_edges))
            return
            
        # If we get here, just make a random move
        self.make_random_move()

    def check_winner(self, highlight=True):
        """Check if there's a winner and highlight winning combination if requested"""
        # Define winning combinations (rows, columns, diagonals)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] != "" and
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                
                # Highlight the winning combination if requested
                if highlight:
                    win_color = "#90EE90"  # Light green
                    for i in combo:
                        self.cells[i].config(bg=win_color)
                
                return True
        
        return False

    def reset_game(self):
        """Reset the game board but keep scores"""
        # Reset board state
        self.board = [""] * 9
        self.current_player = "X"
        self.game_active = True
        
        # Reset UI
        for cell in self.cells:
            cell.config(text="", bg="#ffffff")
            
        # Update status
        self.update_status()

    def reset_scores(self):
        """Reset all scores to zero"""
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        self.update_scores()
        messagebox.showinfo("Scores Reset", "All scores have been reset to zero.")

    def change_game_mode(self, event):
        """Handle game mode change"""
        selected = self.mode_var.get()
        
        if selected == "Human vs Computer":
            self.game_mode = "human_vs_computer"
            self.difficulty_menu.config(state="readonly")
        else:
            self.game_mode = "human_vs_human"
            self.difficulty_menu.config(state="disabled")
            
        # Reset the game when mode changes
        self.reset_game()

    def change_difficulty(self, event):
        """Handle difficulty level change"""
        selected = self.difficulty_var.get().lower()
        self.difficulty = selected
        # Reset the game when difficulty changes
        self.reset_game()


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Create the game
    game = TicTacToe(root)
    
    # Start the main loop
    root.mainloop()
