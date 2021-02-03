#we have to see whether it is palindrome or not?
#1st Method(according to input)
st = 'nayan'
j = -1
count = 0
for i in st:
    if i != st[j]:
      j = j - 1
      count = 1
      break
    j = j - 1
if count == 1:
    print("NO")
else:
    print("Yes")


#2nd Method(num)
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    

#3rd Method(string)
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")