'''we have to find all pairs in the given list whose 
sum is equal to the given num(say-30)'''

num=30
pairs=[]
list1=[10,11,12,13,14,17,18,19,20,21,22,8,7]
list1.sort()
i=0
x=len(list1)
while i<x:
    if list1[i]<num:
        a=num-list1[i]
        if a in list1 and a is not list1[i]:
            pairs.append([list1[i],a])
    i+=1
    x=x-1
print(pairs)




            

             
            
                 

