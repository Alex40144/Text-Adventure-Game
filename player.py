import items, world
import random

class Player():
    def __init__(self):
        self.inventory = [items.Rock()]
        self.hp = 100
        self.victory = False
        self.tile = None

    def is_alive(self):
        return self.hp > 0
    
    def current_tile(self):
        return self.tile


    def move_tile(self, tile):
        self.tile = tile

    def print_inventory(self):
        for item in self.inventory:
            print(item, "\n")


    def attack(self, enemy):
        best_weapon = None
        max_damage = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_damage:
                    best_weapon = i
        
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You have killed {}!".format(enemy.name))
        else:
            print("You did {} damage to {}".format(best_weapon.damage, enemy.name))
            print("{} has {}hp remaining.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)