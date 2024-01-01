n=int(input("Enter number of elements "))
l=[]

for i in range(n):
    a=int(input("enter element "))
    l.append(a)

tuple_string=tuple(map(lambda x:str(x),l))


print(tuple_string)