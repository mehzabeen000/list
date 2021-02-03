#we have to make title function.
a="i am mehzabeen"
i=0
while i<len(a):
    if i==0:
        print(a[i].upper(),end='')
    elif a[i]==' ':
        i+=1
        print('',a[i].upper(),end='')
    else:
        print(a[i],end='')
    i+=1