#we have to sort the list according to the ascending order.

i=0
list1=[5,4,3,2,1]
while i<(len(list1)):
    j=0
    while j<(len(list1) - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        j+=1
    i+=1
print(list1)


#we have to sort the list according to the descending order.
i=0
list1=[1,2,3,4,5]
while i<(len(list1)):
    j=0
    while j<(len(list1) - 1):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        j+=1
    i+=1
print(list1)
