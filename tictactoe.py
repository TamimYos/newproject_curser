board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def show_board():
    """מציג את לוח המשחק."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def has_won(player):
    """בודק אם השחקן השלים שורה, טור או אלכסון."""
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

player = "X"
moves = 0

while True:
    show_board()
    choice = input(f"שחקן {player}, בחר משבצת (1–9): ")

    if not choice.isdigit():
        print("צריך להקליד מספר.")
        continue

    position = int(choice) - 1

    if position < 0 or position > 8:
        print("המספר צריך להיות בין 1 ל־9.")
        continue

    if board[position] == "X" or board[position] == "O":
        print("המשבצת תפוסה. בחר משבצת אחרת.")
        continue

    board[position] = player
    moves += 1

    if has_won(player):
        show_board()
        print(f"שחקן {player} ניצח!")
        break

    if moves == 9:
        show_board()
        print("תיקו!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"