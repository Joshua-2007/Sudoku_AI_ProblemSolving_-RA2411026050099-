# Sudoku_AI_ProblemSolving_-RA2411026050099-
## Interactive Website
[https://joshua-2007.github.io/Sudoku_AI_ProblemSolving_-RA2411026050099-/problem6_sudoku/sudoku.html](https://joshua-2007.github.io/Sudoku_AI_ProblemSolving_-RA2411026050099-RA2411026050091-/problem6_sudoku/)
(sudoku)

https://joshua-2007.github.io/Sudoku_AI_ProblemSolving_-RA2411026050099-RA2411026050091-/problem1_tictactoe/tictactoe.html
(tic tac toe)
## DONE BY JOEL JOSHUA ARUN PEREIRA(RA2411026050099) AND KARTHIK R(RA2411026050091)
📄 Problem 6 Description

This project implements a Sudoku Solver using the Constraint Satisfaction Problem (CSP) approach. A partially filled 9×9 Sudoku grid is provided to the user through an interactive interface. The user can input values into empty cells, and the system validates the solution based on Sudoku rules. Additionally, the system can automatically solve the puzzle using a backtracking algorithm.

🧠 Algorithms Used

The solution is based on Constraint Satisfaction Problem (CSP) techniques.

Backtracking Algorithm
The solver tries numbers from 1 to 9 in empty cells. If a number violates any constraint, it backtracks and tries another value.
Constraint Checking
The following constraints are enforced:
Each row must contain digits 1–9 without repetition
Each column must contain digits 1–9 without repetition
Each 3×3 subgrid must contain digits 1–9 without repetition

▶️ Execution Steps

Open the interactive website (Sudoku interface in browser)
A partially filled Sudoku grid is displayed
Enter values in the empty cells
Click Check to validate your solution
Click Solve to automatically fill the grid
The system displays:
“Solved!” if completed successfully
“Wrong!” if constraints are violated

📊 Sample Output

A 9×9 Sudoku grid displayed in the browser
Pre-filled cells are disabled (cannot be edited)
User-entered values appear in input fields
On clicking Solve, the grid is filled with the correct solution
Alerts/messages displayed:

📄 Problem Description

This project implements an Interactive Tic-Tac-Toe Game with AI. The user plays against a computer opponent on a 3×3 grid through a web-based interface. The system uses an AI algorithm to determine the best possible move, ensuring optimal gameplay. The objective is to either win against the AI or force a draw.

🧠 Algorithms Used

Minimax Algorithm
The AI evaluates all possible future game states and selects the move that maximizes its chances of winning while minimizing the opponent’s chances.
Game Tree Search
All possible moves are explored recursively to determine the optimal decision.

▶️ Execution Steps

Open the interactive website
The game board (3×3 grid) is displayed
Player makes a move by clicking on a cell (X)
The AI automatically responds with its move (O)
The game continues until:
Player wins
AI wins
Draw occurs
Click Restart to play again

📊 Sample Output

Interactive 3×3 grid displayed in browser
Player moves shown as X, AI moves as O
Smooth animations and hover effects
Game result messages:
“You Win!”
“AI Wins!”
“Draw!”
“Solved!” → when solution is correct
“Wrong!” → when constraints are violated
