import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')

seeds = []
data = ''

class ProductionMap:
    def __init__(self, source_category, destination_category):
        self.source_category = source_category
        self.destination_category = destination_category
        self.source_number = []
        self.destination_number = []
        self.range = []

    def add_range(self, source_number, destination_number, range):
        self.source_number.append(source_number)
        self.destination_number.append(destination_number)
        self.range.append(range)

source_category = ''
destination_category = ''

maps = []

with open(input) as f:
    for idx, line in enumerate(f):
        if idx == 0:
            seeds = line.strip().split(' ')[1:]
        elif line == '\n':
            continue
        elif '-to-' in line:  # line contains *-to-* map
            # Extract the *-to-* map
            map_parts = line.strip().split('-to-')
            source_category = map_parts[0].strip()
            destination_category = map_parts[1].strip().split(' ')[0]
            maps.append(ProductionMap(source_category, destination_category))
        else:
            source = int(line.strip().split(' ')[0])
            destination = int(line.strip().split(' ')[1])
            range = int(line.strip().split(' ')[2])
            maps[-1].add_range(source, destination, range)

for seed in seeds:
    for map in maps:
        if 'seed' in map.source_category:
            for idx, source_number in enumerate(map.source_number):
                if int(seed) - source_number + map.range[idx] >= 0:
                    data += seed + ' ' + str(map.destination_number[idx]) + '\n'
                    break


print(data)