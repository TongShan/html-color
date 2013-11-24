from random import randint

board = []

for x in range(0, 15):
    board.append(["O"] * 15)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

guess = False
while guess == False:
    guess_row1 = int(raw_input("A Guess Row:"))
    guess_col1 = int(raw_input("A Guess Col:"))
    guess_row2 = int(raw_input("B Guess Row:"))
    guess_col2 = int(raw_input("B Guess col:"))
    if (guess_col1 == ship_col and guess_row1 == ship_row) or (guess_col2 == ship_col and guess_row2 == ship_row):
        print "Congratulations ! You sank my battleship!"
        break
    else:
        if guess_row1 >= len(board) or guess_col1 >= len(board[0]) or guess_row2 >= len(board) or guess_col2 >= len(board[0]):
            print "Oops, that's not even in the ocean!"
        elif board[int(guess_row1)][int(guess_col1)] == "X" or board[int(guess_row2)][int(guess_col2)] == "Y":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[int(guess_row1)][int(guess_col1)] = "X"
            board[int(guess_row2)][int(guess_col2)] = "Y"

print_board(board)


