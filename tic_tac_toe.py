#table
table = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# we start with player X
player = "X"
# status of the game will be false until win or even
status = False

#check table for win on row, column or diagonal
def check_table(table):
    #check by row
    for item in table:
        if len(set(item)) == 1 and None not in item:
            status = len(set(item)) == 1
            return status
    #check by col
    j = 0
    while j<len(table):
        row=[]
        for r in range(len(table)):
            row.append(table[r][j])
        if len(set(row)) == 1 and None not in row:
            status = (len(set(row)) == 1)
            return status
        j+=1
    #check first diagonal
    j = 0
    row = []
    for item in table:
        row.append(item[j])
        j+=1
    if len(set(row)) == 1 and None not in row:
        status = (len(set(row)) == 1)
        return status
    #check opposite diagonal
    j = len(table[0])-1
    row = []
    for item in table:
        row.append(item[j])
        j-=1
    if len(set(row)) == 1 and None not in row:
        status = (len(set(row)) == 1)
        return status
# check for even result
def check_if_even(table):
    for item in table:
        for el in item:
            if el!="X" and el!="O":
                return False
    return True
# print table
def print_table(table):

    for item in table:
        print("-"*10)
        print(*item,sep=" | ")
    print("-"*10)
# spin the game
while status!=True:
    print(f"Player {player} on move")
    row = int(input("Input row: "))
    column = int(input("Input column: "))

    if table[row][column]!="X" and table[row][column]!="O":
        table[row][column] = player

        status=check_table(table)
        if status==True:
            print(f"Player {player} won")
        else:
            status=check_if_even(table)
            if status==True:
                print(f"Even")
        
        if player == "X":
            player = "O"
        else:
            player = "X"
    
    else:
        print("Cell occupied!")
        print(f"Player {player} on move")
        row = int(input("Input row: "))
        column = int(input("Input column: "))
        if table[row][column]!="X" and table[row][column]!="O":
            table[row][column] = player
    
    print_table(table)



        






