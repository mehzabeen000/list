#we have to print the average of marks in given list

marks=[[10,20,30,40],[10,20,30,40],[10,20,30,40]]
counter=0
sum=0
while counter<len(marks):
    j=0
    count=0
    while j<len(marks[counter]):
        sum+=marks[counter][j]
        count+=1
        j+=1
    counter+=1
print(sum)
print((sum//count), "is the average")

