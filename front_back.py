#we have to see whether the particular list look same form front and behind
a=[1,1,2,1,1]
i=0
mid=len(a)//2
same=True
while i<mid:
    if a[i]!=a[len(a)-i-1]:
        print("No")
        same=False
        break
    i+=1
if same==True:
    print("Yes")
    
