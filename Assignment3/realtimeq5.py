n=int(input("Enter number of elements "))

l=[]

for i in range(n):
    a=int(input("Enter element "))
    l.append(a)

for i in range(n):

    if (l[i]%2==0 and l[i]%3==0):
        print(l[i])
    
