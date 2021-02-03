#we have to see whether the number is in lakhs,crore,thousand etc.
list1=[10000000,300000,10000,20000,73647324,83748,8700,540,32,1]
count_Crorepati=0
count_Lakhpati=0
count_Dilwale=0
for i in list1:
    if i//10000000 or i//100000000:
        count_Crorepati+=1
    elif i//1000000 or i//100000:
        count_Lakhpati+=1
    elif i//10000 or i//1000:
        count_Dilwale+=1
print(count_Crorepati ,"=","Crorepati")
print(count_Lakhpati ,"=","Lakhpati")
print(count_Dilwale, "=","Dilwale1000")