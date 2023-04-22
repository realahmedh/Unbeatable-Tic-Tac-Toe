import tkinter as tk
from tkinter import messagebox

# Set up the game board
board = [' ' for _ in range(9)]

# Set up the root window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg='#1B1B2F')

# Set up the game board frame
board_frame = tk.Frame(root, bg='#1B1B2F')
board_frame.pack(padx=10, pady=10)

# Set up the game status label
status_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 20), fg="#FFFFFF", bg="#1B1B2F")
status_label.pack(pady=10)

# Set up the buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(board_frame, text=' ', font=('Helvetica', 20), width=5, height=2, bg='#4B0082', fg='#FFFFFF', command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

# Set up the player and computer symbols
player_symbol = 'X'
computer_symbol = 'O'

# Set up the minimax algorithm
def minimax(board, depth, is_maximizer):
    if check_winner(board) == 'X':
        return -10 + depth, None
    elif check_winner(board) == 'O':
        return 10 - depth, None
    elif check_draw(board):
        return 0, None

    if is_maximizer:
        best_score = -1000
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer_symbol
                score, _ = minimax(board, depth+1, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move
    else:
        best_score = 1000
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_symbol
                score, _ = minimax(board, depth+1, True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move

# Set up the on button click function
def on_button_click(i, j):
    global board
    global player_symbol
    global computer_symbol

    # Check if the button is already clicked
    if buttons[i][j]['text'] != ' ':
        return

    # Update the game board
    buttons[i][j]['text'] = player_symbol
    board[i*3+j] = player_symbol

    # Check if the game is over
    if check_winner(board) == player_symbol:
        show_message("You win!")
        reset_game()
        return
    elif check_draw(board):
        show_message("Draw!")
        reset_game()
        return

    # Let the computer make a move
    _, move = minimax(board, 0, True)
    buttons[move//3][move%3]['text'] = computer_symbol
    board[move] = computer_symbol

    # Check if the game is over
    if check_winner(board) == computer_symbol:
        show_message("You lose!")
        reset_game()
        return
    elif check_draw(board):
        show_message("Draw!")
        reset_game()
        return

# Set up the check winner function
def check_winner(board):
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != ' ':
            return board[i*3]
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

# Set up the check draw function
def check_draw(board):
    return all([c != ' ' for c in board])

# Set up the show message function
def show_message(message):
    messagebox.showinfo("Game Over", message)

# Set up the reset game function
def reset_game():
    global board
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ' '
    board = [' ' for _ in range(9)]

# Start the game
root.mainloop()