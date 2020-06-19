

_world = {}
starting_position = (0,0)

def load_tiles():
    with open('map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))  #assuming all rows have same length
    for y in range(len(rows)):
        cols = rows[y].split(',')
        for x in range(x_max):
            title_name = cols[x].replace('\n','')
            if title_name == 'StartingRoom':
                global starting_position
                starting_position =(x, y)
            _world[(x,y)] = None if title_name == '' else getattr(__import__('tiles'), title_name)(x,y)

def tile_exists(x,y):
    return _world.get((x,y))