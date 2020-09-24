
#Base class for all in game items
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return "\n=========\n{} - {}\n".format(self.name, self.description)



class Weapon(Item):
    def __init__(self, name, description, found, damage):
        self.damage = damage
        self.found = False
        super().__init__(name, description)
    
    def is_found(self):
        return self.found
    
    def __str__(self):
        return "{} - {} \n======\nDamage: {}".format( self.name, self.description, self.damage)



class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="A simple weapon", found=True, damage=5)

class Pipe(Weapon):
    def __init__(self):
        self.found = False
        super().__init__(name="Pipe", description="A rusty pipe", found=False, damage=6)
