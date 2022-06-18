def show_table(table):
    print(f"\t{table[0]}\t|\t{table[1]}\t|\t{table[2]}")
    print("-------------------------")
    print(f"\t{table[3]}\t|\t{table[4]}\t|\t{table[5]}")
    print("-------------------------")
    print(f"\t{table[6]}\t|\t{table[7]}\t|\t{table[8]}")

# Initial table = Empty table
table = ["X","X","O","O","O","X","O","X","X"]
marks_on_table = 0
show_table(table)

# Control on rows
for column_index in range(0, 9):
    subset = ""

    if column_index == 0 or column_index == 3 or column_index == 6:
        for mark in table[column_index : column_index+3]:
            subset += mark
        if subset == "XXX" or subset == "OOO":
            print(f"Win on row!")
        subset = ""
        column_index += 3

# Control on columns
for row_index in range(0, 9):
    subset = ""
    if row_index == 0 or row_index == 1 or row_index == 2:
        for mark in table[row_index : row_index + 7 : 3]:
            subset += mark
        if subset == "XXX" or subset == "OOO":
            print("Win on Column!")
        subset = ""
        row_index += 3

# Control on diagonals
for diagonal_index in range(0, 9):
    subset = ""
    print(diagonal_index)
    if diagonal_index == 0:
        for mark in table[diagonal_index : diagonal_index + 8 : 3]:
            subset += mark
        if subset == "XXX" or subset == "OOO":
            print("Win on Diagonal!")
        subset = ""

    if diagonal_index == 2:
        for mark in table[diagonal_index : diagonal_index + 5 : 2]:
            subset += mark
        print(f"Subset: {subset}")
        if subset == "XXX" or subset == "OOO":
            print("Win on Diagonal!")
        subset = ""
        diagonal_index += 2







if table[0] + table[1] + table[2] == "XXX" or table[0] + table[1] + table[2] == "OOO":
    print("prima riga tris")
elif table[3] + table[4] + table[5] == "XXX" or table[3] + table[4] + table[5] == "OOO":
    print("seconda riga tris")
elif table[6] + table[7] + table[8] == "XXX" or table[6] + table[7] + table[8] == "OOO":
    print("terza riga tris")

elif table[0] + table[3] + table[6] == "XXX" or table[0] + table[3] + table[6] == "OOO":
    print("prima colonna tris")
elif table[1] + table[4] + table[7] == "XXX" or table[1] + table[4] + table[7] == "OOO":
    print("seconda riga tris")
elif table[2] + table[5] + table[8] == "XXX" or table[2] + table[5] + table[8] == "OOO":
    print("terza riga tris")

elif table[0] + table[4] + table[8] == "XXX" or table[0] + table[4] + table[8] == "OOO":
    print("alto sx-basso dx diagonale tris")
elif table[2] + table[4] + table[6] == "XXX" or table[2] + table[4] + table[6] == "OOO":
    print("alto dx - basso sx diagonale tris")


