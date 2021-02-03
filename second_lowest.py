'''students= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
['Akriti', 41], ['Harsh', 39]] , we have to print the 2 second lowest 
marks'''
    
marksheet=[]
markslist=[]
n=int(input("Enter length"))
for i in range(n):
    name = input("Enter the name")
    marks = float(input("Enter the marks"))
    record=[name,marks]
    marksheet.append(record)
    markslist.append(marks)
marksheet.sort()
s=sorted(set(markslist))[1]
for i,j in marksheet:
    if(j==s):
        print(i) 