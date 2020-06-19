
#Base class for all in game items
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{}\n======\n{}Value: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n======\n{}Value: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="To use, Throw", value=0, damage=5)

class Gold(Item):
    def __init__(self, ammount):
        self.ammount = ammount
        super().__init__(name="Gold", description="A gold coin worth {}".format(str(self.ammount)), value=self.ammount)
