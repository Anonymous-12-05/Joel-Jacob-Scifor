'''
Write a Python Program to find the squares of all the numbers in the given list of integers
using lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

n=int(input("Enter the number of elements "))
l=[]
for i in range(n):
    x=int(input("Enter number "))
    l.append(x)

squares = list(map(lambda x: x**2, l))

for i in squares:
    print(i)
