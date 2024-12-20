# Placement is decided based on numbers 1-9
# top row 1-3, middle row 4-6, and bottom row 7-9

game_on = True

values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print(
        " ", values[0], "|", values[1], "|", values[2], "\n", "-----------", "\n",
        "", values[3], "|", values[4], "|", values[5], "\n", "-----------", "\n",
        "", values[6], "|", values[7], "|", values[8], "\n",
    )


print_board()

while game_on:

    x = int(input("X turn: "))
    if values[x - 1] == " ":
        values[x - 1] = "X"
    else:
        print("Cell already taken, try again.")
        continue

    print_board()

    if (
            (values[0] == values[1] == values[2] == "X") or
            (values[3] == values[4] == values[5] == "X") or
            (values[6] == values[7] == values[8] == "X") or
            (values[0] == values[3] == values[6] == "X") or
            (values[1] == values[4] == values[7] == "X") or
            (values[2] == values[5] == values[8] == "X") or
            (values[0] == values[4] == values[8] == "X") or
            (values[6] == values[4] == values[2] == "X")
    ):
        print("X wins")
        game_on = False
        break

    o = int(input("O turn: "))
    if values[o - 1] == " ":
        values[o - 1] = "O"
    else:
        print("Cell already taken, try again.")
        continue

    print_board()

    if (
            (values[0] == values[1] == values[2] == "O") or
            (values[3] == values[4] == values[5] == "O") or
            (values[6] == values[7] == values[8] == "O") or
            (values[0] == values[3] == values[6] == "O") or
            (values[1] == values[4] == values[7] == "O") or
            (values[2] == values[5] == values[8] == "O") or
            (values[0] == values[4] == values[8] == "O") or
            (values[6] == values[4] == values[2] == "O")
    ):
        print("O wins")
        game_on = False
        break

    if " " not in values:
        print("It's a draw!")
        game_on = False
