
'''
Write a python program to find palindromes in the given list of strings using lambda and
filter function.
['python', 'php', 'aba', 'radar', 'level']
'''
words = []
n=int(input("Enter number of elemets "))
words=[]
for i in range(n):
    a=input("Enter word ")
    words.append(a)

is_palindrome = lambda s: s == s[::-1]
palindromes = list(filter(is_palindrome, words))
print("Palindromes in the list:", palindromes)

