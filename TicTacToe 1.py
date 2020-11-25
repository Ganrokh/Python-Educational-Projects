import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # Vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # Hi-Lo Diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True
    # Lo-Hi Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True



def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is taken! Choose another!")
            return False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return game_map, False
    except Exception as e:
        print(str(e))
        return game_map, False



play = True
while play:
    game_size = int(input("What size game of Tic Tac Toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player=current_player, row=row_choice, column=column_choice)

        if win(game):
            game_won = True
            again = input("The game is over! Play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                print("Thanks for playing!")
                play = False
            else:
                print("Not a valid answer. Sorry, goodbye!")
                play = False