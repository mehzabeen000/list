a=[[5, 3, 4],[ 8, 5, 4], [40, 60, 32]]

i=0
sum=0
while i<len(a):
    sum+=max(a[i])
    i+=1
print(sum,"is the maximum of each list")

