#we have to print the count occurence in the given list

a=['R',2, 'h', 'u', 'S', 1, 'x', 'e', 3,3]

for i in a:
    d=a.count(i)
    if d==1 and d<2:
        print(i ,"-" ,d,"times")
print(i ,"-" ,d,"times")
        
#we have to print the count occurence in the given list without using count function
a=[1,1,2,3,4,5,6,'a',8,5,'a']
b=[]
for i in a:
    if i not in b:
        b.append(i)
n = 0 
list = []
while(n < len(b)):
    j = 0
    count =0
    while j < len(a):
        if b[n] == a[j]:
            count +=1
        j = j + 1
    list.append([b[n], count])
    n = n + 1
print(list)

            