#we have to print the pairs in the list and the specific count of elements
n=[1,2,3,1,2,3,3,4,3,3,3,3]
new=[]
i=0
while i<len(n):
    if n[i] not in new:
        new.append(n[i])
    i+=1
print(new)
count=0
for i in new:
    if i in n:
        d=n.count(i)
        print(i ,"=" ,d, "times")
        if d%2==0:
            count=count+d//2
        if d%2!=0:
            count=count+((d-1)//2)
print(count,"pairs are there in the list")
