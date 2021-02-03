#we have to make remove function
a=[1,2,3,4,5]
count=0
element=int(input("enter "))
for i in range(len(a)):
    if a[i]==element:
        count+=1
    if count>=1:
        pos=a.index(element)
        a1=a[:pos]+a[pos+1:]
print(a1)


