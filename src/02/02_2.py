import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
ouput = os.path.join(current_dir, 'output.txt')
sum = 0


with open(input) as f:
    for line in f:
        game_id = line.split()[1][:-1]
        game_data = line.split(':')[1]
        min_red = 0
        min_green = 0
        min_blue = 0
        for set in game_data.split(';'):
            for color_count in set.split(','):
                count, color = color_count.split()
                if (color == 'red' and int(count) > min_red):
                    min_red = int(count)
                if (color == 'green' and int(count) > min_green):
                    min_green = int(count)
                if (color == 'blue' and int(count) > min_blue):
                    min_blue = int(count)
        sum += min_red * min_green * min_blue
        
print(sum)
