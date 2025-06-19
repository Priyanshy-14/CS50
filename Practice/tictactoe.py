def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers 0-2.")
            continue

        if row not in [0,1,2] or col not in [0,1,2]:
            print("Invalid cell! Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

tic_tac_toe()
