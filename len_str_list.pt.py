#we have to print the length of the string present in the list.

list1=['parveen','shweta','rani']
str=0
count=0
while str<len(list1):
    i=0
    while i<len(list1[str]):
        count+=1
        i+=1
    str+=1
print(count)
