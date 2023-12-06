from math import sqrt, ceil, floor
import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')

tmax_input = []
dmin = []
sum = 1


def clear_input(input: [str]) -> [int]:
    output = []
    for element in input:
        if (element.isdecimal()):
            output.append(int(element))
    return output


with open(input) as f:
    tmax = clear_input(f.readline().strip().split(':')[1].split(' '))
    dmin = clear_input(f.readline().strip().split(':')[1].split(' '))


for i in range(len(tmax)):
    n1 = tmax[i]/2 - (sqrt(-4*dmin[i] + tmax[i]**2))/2
    n2 = tmax[i]/2 + (sqrt(-4*dmin[i] + tmax[i]**2))/2
    if (ceil(n1) == floor(n1)):
        n1 += 1
    if (ceil(n2) == floor(n2)):
        n2 -= 1

    n1 = ceil(n1)
    n2 = floor(n2)
    print(n1, n2)
    print(n2 - n1 + 1)
    
    sum *= (n2 - n1 + 1)


print(sum)
