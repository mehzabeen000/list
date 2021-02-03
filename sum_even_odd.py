'''we have to print the sum of odd numbers and even numbers
respectively'''

list1=[0,2,4,3,5,7,9]
counter=0
sum_even=0
sum_odd=0
while counter<len(list1):
    if list1[counter]%2==0:
        sum_even=sum_even+int(list1[counter])
    elif list1[counter]%2!=0:
        sum_odd =sum_odd+int(list1[counter])
    counter+=1
print(sum_even ,"is the sum of even numbers")
print(sum_odd, "is the sum of odd numbers")
       
