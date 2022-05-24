a=input("Enter string 1:") #listem

b=input("Enter string 2:") #silent

count=0

for i in a: #l

    for j in b: #s

        if i==j: 

            count=count+1

if count==len(a):

    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")
