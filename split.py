#we have to  make split function without using split
#1st ways
a='parveen'
print(list(a))

#2nd ways
list1=['parveen']
for str in list1:
    for i in str:
        print(i)

#3rd ways        
list1=['parveen']
str=0
while str<len(list1):
    i=0
    while i<len(list1[str]):
        print(list1[str][i])
        i+=1
    str+=1
    
