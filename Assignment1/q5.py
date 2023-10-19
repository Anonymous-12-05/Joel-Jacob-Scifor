'''
Write a python program to filter the numbers in a given list that are divisible by 2 and 3
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
'''
n=int(input("Enter the number of elements "))
l=[]
for i in range(n):
    x=int(input("Enter number "))
    l.append(x)

for i in range(n):
    if(l[i]%2==0 and l[i]%3==0):
        print(l[i])


