import items, enemies, actions, world

#base class for all ingame tiles

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return("You have landed on an alien planet. Your sole purpose is to evict the aliens and turn on the master switch.")
    
    def modify_player(self, player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x,y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x,y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyTile(MapTile):
    def intro_text(self):
        return

    def modify_player(self, player):
        pass


#put room types here

class Field(MapTile):
    def intro_text(self):
        return("You find yourself in an empty field.")
    
    def modify_player(self, player):
        pass

class BertTile(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bert())
    def intro_text(self):
        if self.enemy.is_alive:
            return("you come across an alien. His name is Bert")
        else:
            return("A lonely field")

class FindPipeTile(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Pipe())
    def intro_text(self):
        return("You find a rusty pipe in the long grass.")
    