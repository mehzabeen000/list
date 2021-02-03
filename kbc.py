quest=["How many continents are there?" ,"What is the capital of India?",
       "Which subject is taught in navgurukul?"]
options = [[ "1.Four","2.Nine","3.Seven","4.Eight"],
    ["1.Goa","2.Bhopal","3.Chennai","4.Delhi"],
    ["1.Software","2.Tourism","3.Arts","4.Mentorship"]]
lifelist=[["1.Four","2.Seven"],["1.Chennai","2.Delhi"],["1.Software","2.Arts"]]
sol=[3,4,1]
life_ans=[2,2,1]
i=0
count=0
amt=0
while i<len(quest):
    print(quest[i])
    j=0
    while j<=len(options):
        print(options[i][j])
        j+=1
    if count==0:
        lifeline=input("Do you want (50-50) :yes or no. You will get lifeline only once.Choose wisely")
        if lifeline=="yes":
            k=0
            while k<len(lifelist):
                print(lifelist[i][k])
                count+=1
                if k==1:
                    break
                k+=1         
            ans=int(input("Enter your answer"))
            if ans!=life_ans[i]:
                print("Your answer is wrong. You lose")
                break
            else:
                print("Well done")
                amt=amt+i*1000
        else:
            ans=int(input("Enter your answer"))
            if ans!=sol[i]:
                print("Your answer is wrong. You lose")
                break
            else:
                print("Well done")
                amt=amt+i*1000
    else:
        lifeline=input("Do you want (50-50) :yes or no. You will get lifeline only once.Choose wisely")
        if lifeline=="yes":
            print("You have already taken lifeline")
        ans=int(input("Enter your answer"))
        if ans!=sol[i]:
            print("Your answer is wrong. You lose")
            break
        else:
            print("Well done")
            amt=amt+i*1000
                
    i+=1
print("Well done . You have won", amt , "$")

