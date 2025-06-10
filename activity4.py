space1 = " "
space2 = " "
space3 = " "
space4 = " "
space5 = " "
space6 = " "
space7 = " "
space8 = " "
space9 = " "

def print_grid():
    global space1, space2, space3, space4, space5, space6, space7, space8, space9
    print(f"     |     |     ")
    print(f"  {space1}  |  {space2}  |  {space3}  ")
    print(f"     |     |     ")
    print(f"------------------")
    print(f"     |     |     ")
    print(f"  {space4}  |  {space5}  |  {space6}  ")
    print(f"     |     |     ")
    print(f"------------------")
    print(f"     |     |     ")
    print(f"  {space7}  |  {space8}  |  {space9}  ")
    print(f"     |     |     ")

def player1_movement():
    global space1, space2, space3, space4, space5, space6, space7, space8, space9
    player1_move = input("Player X please say which space you want to use >")
    if player1_move == "1" and space1 == " ":
        space1 = "X"
    elif player1_move == "1" and space1 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "2" and space2 == " ":
        space2 = "X"
    elif player1_move == "2" and space2 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "3" and space3 == " ":
        space3 = "X"
    elif player1_move == "3" and space3 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "4" and space4 == " ":
        space4 = "X"
    elif player1_move == "4" and space4 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "5" and space5 == " ":
        space5 = "X"
    elif player1_move == "5" and space5 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "6" and space6 == " ":
        space6 = "X"
    elif player1_move == "6" and space6 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "7" and space7 == " ":
        space7 = "X"
    elif player1_move == "7" and space7 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "8" and space8 == " ":
        space8 = "X"
    elif player1_move == "8" and space8 != " ":
        print("space not available choose another")
        player1_movement()
    if player1_move == "9" and space9 == " ":
        space9 = "X"
    elif player1_move == "9" and space9 != " ":
        print("space not available choose another")
        player1_movement()

def player2_movement():
    global space1, space2, space3, space4, space5, space6, space7, space8, space9
    player2_move = input("Player O please say which space you want to use >")
    if player2_move == "1" and space1 == " ":
        space1 = "O"
    elif player2_move == "1" and space1 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "2" and space2 == " ":
        space2 = "O"
    elif player2_move == "2" and space2 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "3" and space3 == " ":
        space3 = "O"
    elif player2_move == "3" and space3 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "4" and space4 == " ":
        space4 = "O"
    elif player2_move == "4" and space4 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "5" and space5 == " ":
        space5 = "O"
    elif player2_move == "5" and space5 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "6" and space6 == " ":
        space6 = "O"
    elif player2_move == "6" and space6 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "7" and space7 == " ":
        space7 = "O"
    elif player2_move == "7" and space7 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "8" and space8 == " ":
        space8 = "O"
    elif player2_move == "8" and space8 != " ":
        print("space not available choose another")
        player2_movement()
    if player2_move == "9" and space9 == " ":
        space1 = "O"
    elif player2_move == "9" and space9 != " ":
        print("space not available choose another")
        player2_movement()

print_grid()
player1_movement()
print_grid()
player2_movement()
print_grid()
player1_movement()
print_grid()
player2_movement()
print_grid()
player1_movement()
print_grid()
player2_movement()
print_grid()
player1_movement()
print_grid()
player2_movement()
print_grid()
player1_movement()
print_grid()
