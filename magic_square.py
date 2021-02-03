s=[[8,3,4],
   [1,5,9],
   [6,7,2]]
for x in range(0,len(s)):
    if len(s)==len(s[x]):
        pass
    else:
        print("Not a square")
        break
    diag=0
    diag1=0
    for x in range(len(s)):
        diag+=s[x][x]
        y=len(s)-1
        diag1+=s[x][y]
    row=[]
    col=[]
    for x in range(len(s)):
        row_sum=0
        col_sum=0
        for y in range(len(s)):
            row_sum+=s[x][y]
            col_sum+=s[y][x]
        row.append(row_sum)
        col.append(col_sum)
    if row==col:
        if diag==diag1==row[0]==col[0]:
            print("It is a Magic Square")
            break
    else:
        print("It is not a Magic Square")
    


