n=int(input("ENTER A NUMBER:")) #121
temp=n
digit=0
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10

if sum==temp:
    print("ARMS")
else:
    print("NOT")
    
    
