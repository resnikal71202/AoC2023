import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')

i1 = -1
i2 = -1
sum = 0

with open(input) as f:
    for line in f:
        for c in line:
            if c.isdigit():
                if i1 == -1:
                    i1 = int(c)
                i2 = int(c)
        print(i1, i2)
        sum += i1 * 10 + i2
        i1 = -1
        i2 = -1 

print(sum)