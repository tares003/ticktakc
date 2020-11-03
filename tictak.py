board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

player = 1
Win = 1
draw = -1
game_running = 0

game_status = game_running
user_mark = 'X'




def draw_board():
    print(
        f"""
        \n 
        --------------------------------------
        \t  {board[1]}   |  {board[2]}   |  {board[3]}
        --------------------------------------
        \t  {board[4]}   |  {board[5]}   |  {board[6]}
        --------------------------------------
        \t  {board[7]}   |  {board[8]}   |  {board[9]}
        --------------------------------------
        
        """
    )
def check_position(x):
    if (board[x] == ' '):
        return True
    else:
        return False


def check_win():
    global game_status

    # thesea are thesolutions
    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], #horizonatal
                 [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical
                 [1, 5, 9], [3, 5, 7]] # diagonal

    match_found = False
    for s in solutions:
        if board[s[0]] == board[s[1]] and board[s[1]] == board[s[2]] and \
                (board[s[1]] != ' ' or board[s[0]] != ' ' or board[s[1]] != ' ') :
            game_status = Win
            match_found = True

    if not match_found:
        is_draw = False
        for i in board:
            if i != ' ':
                is_draw = True
        if not is_draw:
            game_status = draw
        else:
            game_status = game_running


print("Player 1 [X] --- Player 2 [O]\n")

while game_status == game_running:
    draw_board()
    if (player % 2 != 0): # Modulus check the turns
        print("Player 1's turn")
        user_mark = 'X'
    else:
        print("Player 2's turn")
        user_mark = 'O'
    choice = int(input("Enter the position between 1 - 9 "))
    if check_position(choice):
        board[choice] = user_mark
        player += 1
        check_win()


draw_board()
if (game_status == draw):
    print("game_status draw")
elif (game_status == Win):
    player -= 1
    if (player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")
