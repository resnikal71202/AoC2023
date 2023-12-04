import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')

sum = 0

def number_of_wining_numbers(wining_numbers, numbers):
    count = 0
    for i in numbers:
        if (i in wining_numbers):
            count += 1
    return count


with open(input) as f:
    for line in f:
        line = line.strip('\n')
        line += ' '
        gmae_id = line.split(':')[0].split(' ')[1]
        game_data = line.split(':')[1]
        wining_numbers_string, numbers_string = game_data.split('|')
        wining_numbers = []
        for i in wining_numbers_string.split(' '):
            if (i.isdecimal()):
                wining_numbers.append(int(i))
        numbers = []
        for i in numbers_string.split(' '):
            if (i.isdecimal()):
                numbers.append(int(i))
        thisCount = number_of_wining_numbers(wining_numbers, numbers)
        print(count)
        if (count != 0):
            sum += pow(2, count-1) 
        
print(int(sum))