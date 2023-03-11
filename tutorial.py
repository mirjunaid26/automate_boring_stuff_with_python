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
