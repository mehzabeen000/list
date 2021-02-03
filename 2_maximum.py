#we have to print the second maximum value from the given list
#1st method
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
numbers.sort()
print(numbers[-2])

#2nd method
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.remove(max(numbers))
print(max(numbers))



