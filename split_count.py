'''we have to  make split function without using inbuilt function
and count particular letters in the list(for ex-e in parveen)'''

#for loop
count=0
list1=['parveen']
for str in list1:
    for i in str:
        if i=='e':
            count+=1
print(count, "times e occured")

#while loop    
list1=['parveen']
str=0
while str<len(list1):
    i=0
    count=0
    while i<len(list1[str]):
        if list1[str][i]=='e':
            count+=1
        i+=1
    str+=1
print(count, "times e occured")
