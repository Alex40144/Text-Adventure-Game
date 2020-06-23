import csv

_world = {}
map = []
starting_position = (0,0)

def load_tiles():
    datareader = csv.reader(open('map.csv', 'r'), delimiter=',')
    for row in datareader:
        map.append(row)

    x_max = len(map[0])
    y_max = len(map)

    for x in range(x_max):
        for y in range(y_max):
            tile_name = str(map[y][x])
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x,y):
    return _world.get((x, y))