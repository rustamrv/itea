import random

def random_number(num):
    start = 0 
    while start < num:
        yield random.randint(0, 100) 
        start += 1


numbers = random_number(10)
for i in numbers:
    print(i)