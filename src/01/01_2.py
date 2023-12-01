import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
ouput = os.path.join(current_dir, 'output.txt')
str_numbers = ['one', 'tw', 'thre', 'four', 'fiv', 'six', 'seve', 'igh', 'nin']

with open(input) as f:
    with open(ouput, 'w') as f2:
        for line in f:
            for i in range(9):
                line = line.replace(str_numbers[i], str(i+1))
            f2.write(line)

i1 = -1
i2 = -1
sum = 0

with open(ouput) as f:
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