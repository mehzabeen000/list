#we have to print the maximum number in the given list

#1st way:
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
print(max(numbers))

#2nd way:
a=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
maximum=a[0]
i=0
while i<len(a):
  if a[i]>maximum:
      maximum=a[i]
  i = i+1
print(maximum)

#we have to print the minimum number in the given list
a=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
minimum=a[0]
i=0
while i<len(a):
    if a[i]<minimum:
        minimum=a[i]
    i+=1
print(minimum)

