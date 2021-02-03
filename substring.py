#we have to remove the substring from the given list.
mainstr="Tarun is a naughty girl and i want to beat her"
substr="beat"
mainstr=mainstr.split()
for list1 in mainstr:
    if list1==substr:
        mainstr.remove(list1)
print(mainstr)

#we have to replace the substring from the given list.
mainstr="Tarun is a naughty girl and i want to beat her"
substr="beat"
replace="kick"
var=mainstr.split()
i=0
b=' '
while i<len(var):
    if var[i] == substr:
         b = b+ replace + ' '
    else:
        b = b+ var[i] + ' '
    i+=1
print(b)

