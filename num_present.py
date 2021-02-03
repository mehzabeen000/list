'''we have 2 arrays and we have to find which numbers
are not present in the first array'''
#1st Method
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
print((set(list1))-(set(list2)))

#2nd Method
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
new_list=[]
counter=0
while counter<len(list1):
    if list1[counter] not in list2:
        new_list.append(list1[counter])
    counter+=1
print(new_list)
