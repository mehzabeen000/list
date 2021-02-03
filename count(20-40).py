#we have to print the count of elements which are greater than 20 and lesser then 40

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
count=0
for i in numbers:
    if i>=20 and i<=40:
        count+=1
        continue
print(count)
 


        
        