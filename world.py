import tiles, sys


def next_tile(tile):
    return get_tile(tile)

def get_tile(tilename):
    return getattr(tiles, tilename)