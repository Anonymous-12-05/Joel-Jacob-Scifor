#default arguments
def fun(a=10,b=20):
    return a+b
#keyword arguments
def sub(a,b):
    return a-b

#variable length arguments
def func(*args):
    for arg in args:
        print(arg)

#lambda function
y=lambda x:x**2
print(y(2))

print(fun(15))

print(sub(a=10,b=5)) 

print(func(1,2,3,4,))  