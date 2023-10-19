''' Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli',
24936)]
'''

n=int(input("Enter number of elements "))
l=[]
for i in range(n):
    name=input("Enter name ")
    num=int(input("Enter number "))

    l.append((name,num))


sorted_data = sorted(l, key=lambda x: x[1])

for item in sorted_data:
    print(item)
