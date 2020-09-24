import tiles, sys


def next_tile(tiles):
    if len(tiles) == 1:
        next_tile =  tiles
        return get_tile(next_tile[0])

def get_tile(tilename):
    return getattr(tiles, tilename)