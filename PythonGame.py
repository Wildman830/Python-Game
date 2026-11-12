from time import sleep

def load_board(display):
    plus = 0 - 1
    for row in display:
        for col in row:
            print(col + "  ", end= "")
        plus += 1
        print("")
    for plus1 in range(plus):
        print(str(plus1 + 1) + "  ", end= "")
    print("")

def drop_piece(player_in, col, game): #drops pieces in place based on the input
    for row in range(BOARD_HEIGHT + 1):
        if row == BOARD_HEIGHT: #places on bottom if checker passes board
            game[row - 1][col] = player_in
            return game, row -1, col
        if game[row][col] == "R" or game[row][col] == "Y" : #places above if another piece is placed
            game[row - 1][col] = player_in
            return game, row -1, col


def validate(player_in, col): #makes sure user input is valid
    if player_in != "Y" and player_in != "R":
        print("Invalid Player")
        return False
    if col <= -1 or col > BOARD_WIDTH: # if col not in range(1, BOARD_WIDTH + 1)
        print("Invalid Column")
        return False
    if game[0][col] == "R" or game[0][col] == "Y":
        print("bad boy")
        return False
    return True

#Cross
def check_bot_middle(x, y, checked_game, player_in):
    if checked_game[x + 1][y] == player_in:
        return True
    else:
        return False
def check_mid_right(x, y, checked_game, player_in):
    if checked_game[x][y + 1] == player_in:
        return True
    else:
        return False
def check_mid_left(x, y, checked_game, player_in):
    if checked_game[x][y - 1] == player_in:
        return True
    else:
        return False
def check_top_middle(x, y, checked_game, player_in):
    if checked_game[x - 1][ y] == player_in:
        return True
    else:
        return False


#Diagonal
def check_top_left(x, y, checked_game, player_in):
    if checked_game[x - 1][ y - 1] == player_in:
        return True
    else:
        return False
def check_top_right(x, y, checked_game, player_in):
    if checked_game[x - 1][ y + 1] == player_in:
        return True
    else:
        return False
def check_bot_left(x, y, checked_game, player_in):
    if checked_game[x + 1][ y - 1] == player_in:
        return True
    else:
        return False
def check_bot_right(x, y, checked_game, player_in):
    if checked_game[x + 1][ y + 1] == player_in:
        return True
    else:
        return False

def check_win(x, y, checked_game, player_in):
    cross_hori = 0
    cross_veri = 0
    diagonal_tlbr = 0
    diagonal_trbl = 0
    temp_x, temp_y = x, y

    #Top left to bottom right
    try:
        while check_top_left(temp_x, temp_y, checked_game, player_in):
            diagonal_tlbr += 1
            temp_x, temp_y = temp_x - 1, temp_y - 1
    except:
        pass
    temp_x, temp_y = x, y
    try:
        while check_bot_right(temp_x, temp_y, checked_game, player_in):
            diagonal_tlbr += 1
            temp_x, temp_y = temp_x + 1, temp_y + 1
    except:
        pass
    temp_x, temp_y = x, y

    #Top right to bottom left
    try:
        while check_top_right(temp_x, temp_y, checked_game, player_in):
            diagonal_trbl += 1
            temp_x, temp_y = temp_x - 1, temp_y + 1
    except:
        pass
    temp_x, temp_y = x, y
    try:
        while check_bot_left(temp_x, temp_y, checked_game, player_in):
            diagonal_trbl += 1
            temp_x, temp_y = temp_x + 1, temp_y - 1
    except:
        pass
    temp_x, temp_y = x, y


    #Horizontal
    try:
        while check_mid_left(temp_x, temp_y, checked_game, player_in):
            cross_hori += 1
            temp_x, temp_y = temp_x , temp_y - 1
    except:
        pass
    temp_x, temp_y = x, y
    try:
        while check_mid_right(temp_x, temp_y, checked_game, player_in):
            cross_hori += 1
            temp_x, temp_y = temp_x, temp_y + 1
    except:
        pass
    temp_x, temp_y = x, y

    #Vertical
    try:
        while check_top_middle(temp_x, temp_y, checked_game, player_in):
            cross_veri += 1
            temp_x, temp_y = temp_x - 1, temp_y
    except:
        pass
    temp_x, temp_y = x, y
    try:
        while check_bot_middle(temp_x, temp_y, checked_game, player_in):
            cross_veri += 1
            temp_x, temp_y = temp_x + 1, temp_y
    except:
        pass
    temp_x, temp_y = x, y
    if cross_veri > 2 or cross_hori > 2 or diagonal_tlbr > 2 or diagonal_trbl > 2:
        return True, player_in
    return False, player_in

def play(player, game_board, won):
    load_board(game_board)
    player = player.upper()
    played_col = int(input(player + " drop: ")) -1
    if validate(player, played_col) == False:
        sleep(3.5)
        return win, player_win
    game_board, placed_x, placed_y = drop_piece(player, played_col, game)
    won, player_win = check_win(placed_x, placed_y, game, player)
    return won, player_win, game_board

    

    
BOARD_HEIGHT = 7
BOARD_WIDTH = 6
win = False
game = [["*" for x in range(BOARD_WIDTH)]for y in range(BOARD_HEIGHT)]
placed_x = -1
placed_y = -1
player_win = "null"
player = "null"
x = 0

while win != True:
    if x % 2 == 0 :
        player = "Y"
    else:
        player = "R"
    win, player_win, game = play(player, game, win)
    x += 1
load_board(game)
print(player_win + " Won")


# friendly notes:
# offsets = [[1,0],[0, 1],[-1,0],[0,-1]]
# for offset in offsets
# if checked_game[x + offset[0], y + offset[1]]:
#    return 1
# else:
#   return 0