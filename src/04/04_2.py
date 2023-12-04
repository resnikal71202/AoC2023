import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')

sum = 0
count = []

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
        count.append(number_of_wining_numbers(wining_numbers, numbers))

card_count = [1] * len(count)

for idx, j in enumerate(count):
    for i in range(count[idx]):
        card_count[i+1 + idx] += card_count[idx]
    print(card_count)

for i in card_count:
    sum += i

print(sum)