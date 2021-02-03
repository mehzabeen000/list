#we have to print the length of even count of particular lists

a=[["Mehzabeen"],["Navgurukul"],["12345678"]]
str=0
while str<len(a):
    i=0
    count=0
    while i<len(a[str]):
        j=0
        while j<len(a[str][i]):
            count+=1
            j+=1    
        i+=1
        if count%2==0:
            print(count,"=", a[str])
    str+=1

   
