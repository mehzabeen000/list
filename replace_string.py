replace="T"
b=''
list1=['mehzabeen','karuna','sheetal']
str=0
while str<len(list1):
    i=0
    while i<len(list1[str]):
        if list1[str][i]=="m":
          b=b+replace+''
        else:
            b=b+list1[str][i]+'' 
        i+=1
    b=b + ' '
    str+=1
print(b)


replace="TT"
b=''
list1=['mehzabeen','karuna','sheetal']
str=0
while str<len(list1):
    i=0
    while i<len(list1[str]):
        if list1[str][i]=="a":
          b=b+replace+''
        else:
            b=b+list1[str][i]+'' 
        i+=1
    b=b+' '
    str+=1
print(b)

