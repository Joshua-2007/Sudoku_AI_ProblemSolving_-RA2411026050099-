import tkinter as tk
from tkinter import messagebox

# ----------- COLORS -----------
BG_COLOR = "#1e1e2f"
CELL_COLOR = "#ffffff"
FIXED_COLOR = "#d1d5db"
TEXT_COLOR = "#000000"
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT = "#ffffff"

# Pre-filled Sudoku
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

entries = []

# ----------- VALIDATION -----------

def is_valid(board):
    for row in board:
        nums = [n for n in row if n != 0]
        if len(nums) != len(set(nums)):
            return False

    for col in range(9):
        nums = []
        for row in range(9):
            if board[row][col] != 0:
                nums.append(board[row][col])
        if len(nums) != len(set(nums)):
            return False

    for box_row in range(3):
        for box_col in range(3):
            nums = []
            for i in range(3):
                for j in range(3):
                    val = board[3*box_row+i][3*box_col+j]
                    if val != 0:
                        nums.append(val)
            if len(nums) != len(set(nums)):
                return False

    return True

# ----------- SOLVER -----------

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    board[row][col] = num
                    if is_valid(board) and solve_sudoku(board):
                        return True
                    board[row][col] = 0
                return False
    return True

# ----------- GUI FUNCTIONS -----------

def load_grid():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                entries[i][j].insert(0, str(grid[i][j]))
                entries[i][j].config(state='disabled', bg=FIXED_COLOR)

def get_user_grid():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board

def check_solution():
    board = get_user_grid()
    if is_valid(board) and all(all(cell != 0 for cell in row) for row in board):
        messagebox.showinfo("Result", "🎉 You win!")
    else:
        messagebox.showerror("Result", "❌ Try again!")

def solve():
    board = get_user_grid()
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].config(state='normal')
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
        messagebox.showinfo("Solved", "✨ Solution displayed!")
    else:
        messagebox.showerror("Error", "No solution exists")

# ----------- WINDOW -----------

root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg=BG_COLOR)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(padx=10, pady=10)

for i in range(9):
    row = []
    for j in range(9):
        border_x = 2 if j % 3 == 0 else 1
        border_y = 2 if i % 3 == 0 else 1

        e = tk.Entry(
            frame,
            width=3,
            font=('Arial', 20, 'bold'),
            justify='center',
            bg=CELL_COLOR,
            fg=TEXT_COLOR,
            relief="solid",
            bd=border_x
        )
        e.grid(row=i, column=j, padx=(border_x,1), pady=(border_y,1))
        row.append(e)
    entries.append(row)

load_grid()

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Check", command=check_solution,
          bg=BUTTON_COLOR, fg=BUTTON_TEXT, width=10).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Solve", command=solve,
          bg=BUTTON_COLOR, fg=BUTTON_TEXT, width=10).grid(row=0, column=1, padx=5)

root.mainloop()