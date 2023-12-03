import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
ouput = os.path.join(current_dir, 'output.txt')
sum = 0


def break_condition(color, count):
    """only 12 red cubes, 13 green cubes, and 14 blue cubes"""
    if color == 'red' and count > 12:
        return True
    if color == 'green' and count > 13:
        return True
    if color == 'blue' and count > 14:
        return True
    return False


with open(input) as f:
    for line in f:
        game_id = line.split()[1][:-1]
        game_data = line.split(':')[1]
        break_flag = False
        for set in game_data.split(';'):
            for color_count in set.split(','):
                count, color = color_count.split()
                if (break_condition(color, int(count))):
                    break_flag = True
                    break
            if break_flag:
                break
        if not break_flag:
            sum += int(game_id)

print(sum)
