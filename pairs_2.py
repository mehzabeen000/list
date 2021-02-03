'''we have to count the number 2 in the given list'''

num=[1,2,3,4,2,2,2,2]
counter=0
count=0
while counter<len(num):
    if num[counter]==2:
        count+=1
    if count%2==0:
        count//2    
    counter+=1
print((count//2),"pairs are there")