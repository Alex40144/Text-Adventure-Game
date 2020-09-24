from player import Player
import world


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveToTile(Action):
    def __init__(self, tile, tilename, hotkey):
        self.tile = tile
        self.tilename = tilename
        self.hotkey = hotkey
        super().__init__(method=Player.move_tile, name=tilename, hotkey=hotkey, tile=tile)


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View Inventory', hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)
