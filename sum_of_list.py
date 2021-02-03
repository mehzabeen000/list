#we have to print the sum of 3 years given in list
marks=[[78,76,94,86,88], [91,71,98,65,76],[95,45,78,52,49]]
sum=0
counter=0
while counter<len(marks):
    i=0
    while i<len(marks[counter]):
        sum+=marks[counter][i]
        i+=1
    counter+=1
print(sum)



