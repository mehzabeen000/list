#we have to remove duplicates and print them in another list
n=[11,12,12,21,32,12,16,17,17,17]
i=0
new_list=[]
duplicates=[]
while i<len(n):
    if n[i] not in new_list:
        new_list.append(n[i])
    else:
        duplicates.append(n[i])
    i+=1
print(duplicates)
        