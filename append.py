#we have to make append function

a=[1,2,3,4,5]
element=int(input("enter "))
for i in range(len(a)):
    a=a+[element]
    break
print(a)
