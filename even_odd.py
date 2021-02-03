'''we have to print the odd numbers and even numbers
separetely'''

list1=[0,2,4,3,5,7,9]
i=0
while i<len(list1):
    if list1[i]%2==0:
        print('even','=', list1[i])
    elif list1[i]%2!=0:
        print('odd' ,'=',list1[i])
    i+=1
        
