#tabela
table = [[1, 2, 1],
         [2, 1, 2],
         [2, 1, 2]]
#igrac

player = "x"
status = False
#provjera statusa igre, win loose even
#moguci nacini za pobjedu

def check_table(table):
    #check by row
    for item in table:
        if len(set(item)) == 1 and None not in item:
            status = len(set(item)) == 1
            # print (f"Row {table.index(item)} {status}")
            return status
    #check by col
    j = 0
    while j<len(table):
        row=[]
        for r in range(len(table)):
            row.append(table[r][j])
        if len(set(row)) == 1 and None not in row:
            status = (len(set(row)) == 1)
            # print (f"Column {str(j)} {status}")
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
        # print (f"First diagonal {status}")
        return status
    #check opposite diagonal
    j = len(table[0])-1
    row = []
    for item in table:
        row.append(item[j])
        j-=1
    if len(set(row)) == 1 and None not in row:
        status = (len(set(row)) == 1)
        # print (f"Opposite diagonal {status}")
        return status

def check_if_even(table):
    for item in table:
        if None not in item:
            return True






