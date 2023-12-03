import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
data = []
sum = 0


def test_for_symbol(data, rindex, idx):
    if (idx != 0):
        if (data[rindex][idx-1] != '.' and not data[rindex][idx-1].isdecimal()):
            return True
    if (idx != len(data[rindex])-1):
        if (data[rindex][idx+1] != '.' and not data[rindex][idx+1].isdecimal()):
            return True
    if (rindex != 0):
        if (data[rindex-1][idx] != '.' and not data[rindex-1][idx].isdecimal()):
            return True
    if (rindex != len(data)-1):
        if (data[rindex+1][idx] != '.' and not data[rindex+1][idx].isdecimal()):
            return True
    if (rindex != 0 and idx != 0):
        if (data[rindex-1][idx-1] != '.' and not data[rindex-1][idx-1].isdecimal()):
            return True
    if (rindex != len(data)-1 and idx != len(data[rindex])-1):
        if (data[rindex+1][idx+1] != '.' and not data[rindex+1][idx+1].isdecimal()):
            return True
    if (rindex != 0 and idx != len(data[rindex])-1):
        if (data[rindex-1][idx+1] != '.' and not data[rindex-1][idx+1].isdecimal()):
            return True
    if (rindex != len(data)-1 and idx != 0):
        if (data[rindex+1][idx-1] != '.' and not data[rindex+1][idx-1].isdecimal()):
            return True
    return False


with open(input) as f:
    for line in f:
        line = line.strip('\n')
        data.append(line)

for rindex, row in enumerate(data):
    for idx, i in enumerate(row):
        if (i.isdecimal() and not row[idx-1].isdecimal()):
            j = int(idx)
            while (j < len(row) and row[j].isdecimal()):
                j += 1
            flag = False
            for k in range(idx, j):
                if (test_for_symbol(data, rindex, k)):
                    flag = True
                    break
            if (flag):
                sum += int(row[idx:j])

print(sum)
