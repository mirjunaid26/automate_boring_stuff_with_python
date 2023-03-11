# print("Hello PyCharm")

def next_year():
    global year
    print("The current year is: ", year)
    year += 1
    print("The next year will be: ", year)

year = 2023
next_year()
