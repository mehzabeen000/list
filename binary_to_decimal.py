b_num = list(input("Input a binary number: "))
value = 0
for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + (2**i)
print(value)

    

total = 0
numb = (input("Enter your whole binary number: "))
for i in range (1, (numb.__len__())+1):
   if numb[-i] == str(1):
        total = total + (2**(i-1))
print(total)

