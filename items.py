
#Base class for all in game items
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{} - {}\n======\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{} - {} \n======\nDamage: {}".format( self.name, self.description, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="A simple weapon", value=0, damage=5)

class Pipe(Weapon):
    def __init__(self):
        super().__init__(name="Pipe", description="A rusty pipe", value=0, damage=6)

class Gold(Item):
    def __init__(self, ammount):
        self.ammount = ammount
        super().__init__(name="Gold", description="An item that can be used for nothing", value=self.ammount)
