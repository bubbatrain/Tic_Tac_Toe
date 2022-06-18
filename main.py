# TIC TAC TOE GAME
'''
This is a classic game for two players.
Players put their marks on the game table, trying to get 3 marks
in a row (up, down, across, diagonally).
'''

# This function shows the actual game table.
# It is a visual representation of the marks inside the 'table' list.
def show_table(table):
    print(f"\t{table[0]}\t|\t{table[1]}\t|\t{table[2]}")
    print("-------------------------")
    print(f"\t{table[3]}\t|\t{table[4]}\t|\t{table[5]}")
    print("-------------------------")
    print(f"\t{table[6]}\t|\t{table[7]}\t|\t{table[8]}")


# This function checks if there are 3 identical marks in a row.
# It checks all the possible winning combinations on rows, columns, and
# diagonals.
# In order to do this, various subsets of the 'table' list are extracted
# using a slicing technique with different indexes.
# These subsets are then compared to the winning subsets ('XXX' or 'OOO').
# Return true if comparison is True
def is_tris(table):
    # Control on rows
    for column_index in range(0, 9):
        subset = ""
        if column_index == 0 or column_index == 3 or column_index == 6:
            for mark in table[column_index: column_index + 3]:
                subset += mark
            if subset == "XXX" or subset == "OOO":
                print(f"\nWin on row!")
                return True

    # Control on columns
    for row_index in range(0, 9):
        if row_index == 0 or row_index == 1 or row_index == 2:
            for mark in table[row_index: row_index + 7: 3]:
                subset += mark
            if subset == "XXX" or subset == "OOO":
                print("\nWin on Column!")
                return True

    # Control on diagonals
    for diagonal_index in range(0, 9):
        subset = ""
        if diagonal_index == 0:
            for mark in table[diagonal_index: diagonal_index + 8: 3]:
                subset += mark
            if subset == "XXX" or subset == "OOO":
                print("\nWin on Diagonal!")
                return True

        if diagonal_index == 2:
            for mark in table[diagonal_index: diagonal_index + 5: 2]:
                subset += mark
            if subset == "XXX" or subset == "OOO":
                print("\nWin on Diagonal!")
                return True


# This function ask players for position where they want to put their mark,
# validates this position and make a mark at that position.
# The mark is stored in the 'table' list and the position index.
def player_turn(table, marks_on_table, player_number):
    marks = {
        1: "X",
        2: "O"
    }
    can_put = False
    while not can_put:
        position = input(f"\nPlayer {player_number}, where do you want to put the {marks[player_number]} ?:")

        if not position.isnumeric():
            print("Please select a valid position.")

        elif int(position) < 0 or int(position) > 8:
            print("Invalid position. Please select another position.")

        elif table[int(position)] == "X" or table[int(position)] == "O":
            print(f"Position {int(position)} is already marked. Please select another position.")

        else:
            can_put = True
            table[int(position)] = marks[player_number]
            marks_on_table += 1
            return table


# Shows players instructions of the game
print("\n*******  INSTRUCTIONS:   *******"
      "\n1. The game is played on a grid that's 3 squares by 3 squares."
      "\n2. Player 1'mark is X, Player 2'mark is O. Players take turns putting their marks in empty squares."
      "\n3. The first player to get 3 of his marks in a row (up, down, across, or diagonally) is the winner."
      "\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie."
      "\n5. To put your mark, please select the position on the grid using a numeric value, following the layout "
      "below:\n")

# Initialize 'table' list to display positions
instructions_table = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
show_table(instructions_table)
print("\n\n\n")

# Initialize table with an empty list
table = ["", "", "", "", "", "", "", "", ""]
show_table(table)

# Counter of marks
marks_on_table = 0

# Main loop of the app
should_quit = False
while not should_quit:

    # Check which player has to put the mark.
    # Even rounds -> Player 1
    # Odd rounds -> Player 2
    if marks_on_table < 9:
        if marks_on_table % 2 == 0:
            selected_player = 1
        else:
            selected_player = 2

        # Asking player for position of his mark.
        table = player_turn(table, marks_on_table, selected_player)

        # Incrementing count of marks on table
        marks_on_table += 1

        # Shows updated game table
        print("\n")
        show_table(table)

        # Check if there is a winner
        if is_tris(table):
            print(f"\nPlayer {selected_player} wins!")
            should_quit = True

    # When game table is full and there are no winners, game end with a tie.
    else:
        print("\nGame is over. It's a tie.")
        should_quit = True