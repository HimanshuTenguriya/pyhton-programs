a=input()
a=a.split(",")
b="" #a
c=0  #b
d=0  #c
for x in a:
    for y in a:
        if(y==x):
                c=c+1
    if(c>d):
        b=x
        d=c
    c=0    
print(b)
