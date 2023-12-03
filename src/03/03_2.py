import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
data = []
sum = 0


def test_gear_for_numbers(data, rindex, idx):
    number_pos = []
    if (idx != 0):
        if (data[rindex][idx-1].isdecimal()):
            number_pos.append((rindex, idx-1))
    if (idx != len(data[rindex])-1):
        if (data[rindex][idx+1].isdecimal()):
            number_pos.append((rindex, idx+1))
    if (rindex != 0):
        if (data[rindex-1][idx].isdecimal()):
            number_pos.append((rindex-1, idx))
    if (rindex != len(data)-1):
        if (data[rindex+1][idx].isdecimal()):
            number_pos.append((rindex+1, idx))
    if (rindex != 0 and idx != 0):
        if (data[rindex-1][idx-1].isdecimal()):
            number_pos.append((rindex-1, idx-1))
    if (rindex != len(data)-1 and idx != len(data[rindex])-1):
        if (data[rindex+1][idx+1].isdecimal()):
            number_pos.append((rindex+1, idx+1))
    if (rindex != 0 and idx != len(data[rindex])-1):
        if (data[rindex-1][idx+1].isdecimal()):
            number_pos.append((rindex-1, idx+1))
    if (rindex != len(data)-1 and idx != 0):
        if (data[rindex+1][idx-1].isdecimal()):
            number_pos.append((rindex+1, idx-1))
    return clear_number_pos(number_pos)

def clear_number_pos(number_pos):
    for i,j in number_pos:
        for k,l in number_pos:
            if (i == k and j == l):
                continue
            if (i == k):
                if (j == l-1 or j == l+1):
                    number_pos.remove((k,l))
            if (j == l):
                if (i == k-1 or i == k+1):
                    number_pos.remove((k,l))
    return number_pos


def get_number(data, rindex, idx):
    number = []
    for i in range(idx, len(data[rindex])):
        if (data[rindex][i].isdecimal()):
            number.append(data[rindex][i])
        else:
            break
    for i in range(idx-1, -1, -1):
        if (data[rindex][i].isdecimal()):
            number.insert(0, data[rindex][i])
        else:
            break
    return int(''.join(number))


with open(input) as f:
    for line in f:
        line = line.strip('\n')
        data.append(line)


for rindex, row in enumerate(data):
    for idx, i in enumerate(row):
        if (i == '*'):
            number_positions = test_gear_for_numbers(data, rindex, idx)
            if (len(number_positions) == 2):
                num1 = get_number(data, number_positions[0][0], number_positions[0][1])
                num2 = get_number(data, number_positions[1][0], number_positions[1][1])
                sum += num1 * num2

print(sum)
