import random

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid range. Choose 1-9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Enter a number.")

def bot_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    mode = input("Choose mode: 1 for Player vs Player, 2 for Player vs Bot: ")
    current = "X"

    while True:
        print_board(board)
        if mode == "2" and current == "O":
            print("Bot is thinking...")
            row, col = bot_move(board)
        else:
            row, col = get_move(board, current)

        board[row][col] = current

        if check_win(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"

play_game()