import items, enemies, actions, world, player

#base class for all ingame tiles

class MapTile:
    def __init__(self):
        pass

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()
    
    #this defines the next tiles that a player can move to.
    def next_tile(self):
        raise NotImplementedError()

    def available_actions(self):
        moves = self.next_tile()
        for i in range(0, len(moves)):
            moves[i] = actions.MoveToTile(moves[i][0], moves[i][1], moves[i][2])
        
        #removed this for now, won't need it for a while
        #moves.append(actions.ViewInventory())

        return moves


#if the player needs anything
class LootRoom(MapTile):
    def __init__(self, item):
        self.item = item
        super().__init__()

    def add_loot(self, player):
        if self.item not in player.inventory:
            player.inventory.append(self.item)
            print("you found a " + self.item.name)
        else:
            self.item.count += 1
            print("you found a " + self.item.name)


    def modify_player(self, player):
        self.add_loot(player)


#This will probaby be used later in the story
class EnemyRoom(MapTile):
    def __init__(self, enemy):
        self.enemy = enemy
        super().__init__()

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} does {} damage to you. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            pass

class EmptyTile(MapTile):
    def intro_text(self):
        pass

    def modify_player(self, player):
        pass


#put room types here

class StartingRoom(MapTile):
    def intro_text(self):
        return("Welcome to the Ready Player One simulation. Play as Wade Watts as you adventure through the oasis")
    
    def modify_player(self, player):
        return False

    def next_tile(self):
        return [[world.next_tile(["Halliday"]), "Next", "n"]]


class Halliday(MapTile):
    def intro_text(self):
        return("This is the bit where Halliday say's he is dead")

    def modify_player(self, player):
        return False

    def next_tile(self):
        return [[world.next_tile(["EmptyTile"]), "Empty tile", "e"]]





