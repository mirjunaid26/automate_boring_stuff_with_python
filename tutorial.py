# The Python Tutorial
"""
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
"""
# Numbers
a = 2
b = 3
c = a + b
print(c)

tax = 12.5 / 100
price = 100.50
d = price * tax
print(d)

# Strings
a = 'spam eggs'
print(a)

b = ' "Yes," they said.'
print(b)

# Lists
squares = [1, 2, 3, 4]
print(squares)
print(squares[-1])
print(squares[-2])
print(squares[3])

squares += [5, 6, 7, 8]
print(squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
print(letters[:])
print(letters[:0])
print(letters[:1])
print(letters[:2])
print(letters[:-1])
print(letters[:-2])

print(len(letters))

# First Steps Towards Programming

# Fibonacci series
a = 0
b = 1

while a < 100:
    print(a)
    a = b
    b = a + b

# keyword end argument
a = 0
b = 1
while a < 1000:
    print(a, end=',') # keyword end is used to avoid new line
    a, b = b, a+b

print("New Branch")

# Control Flow Tools

# Measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection

users = {'Hans': 'active', 'Eleonore': 'inactive', 'Mir': 'active'}
print("All users: ", users)
# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print("Active Users: ", users)

# Strategy: Create a new collection

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# range function

a = ['Marry', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

x = sum(range(4))
print(x)
