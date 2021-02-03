'''we have to print the average and sum of even,
odd and all numbers'''
list1=[0,2,4,3,5,7,9]
counter=0
sum_even=0
sum_odd=0
even_count=0
odd_count=0
while counter<len(list1):
    if list1[counter]%2==0:
        sum_even=sum_even+int(list1[counter])
        even_count+=1
    elif list1[counter]%2!=0:
        sum_odd =sum_odd+int(list1[counter])
        odd_count+=1
    counter+=1
all_sum=sum_even+sum_odd
all_count=even_count+odd_count
avg_even=sum_even//even_count
avg_odd=sum_odd//odd_count
avg_all=all_sum//all_count
print(all_sum ,"is the sum of all numbers")
print(sum_even, "is the sum of even numbers")
print(sum_odd, "is the sum of odd numbers")
print(avg_even ,"is the average of even numbers")
print(avg_odd, "is the average of odd numbers")
print(avg_all, "is the average of all numbers")
