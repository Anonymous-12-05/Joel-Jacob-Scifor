'''
Write a python program to convert the given list of integers into a tuple of strings. Use map
and lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
'''
n=int(input("Enter the number of elements "))
l=[]
for i in range(n):
    x=int(input("Enter number "))
    l.append(x)

strings = tuple(map(lambda x: str(x), l))


print(strings)