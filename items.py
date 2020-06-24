
#Base class for all in game items
class Item():
    def __init__(self, name, description, found):
        self.name = name
        self.description = description
    
    def __str__(self):
        return "\n=========\n{} - {}\n".format(self.name, self.description)

    def is_found(self):
        return self.found


class Weapon(Item):
    def __init__(self, name, description, found, damage):
        self.damage = damage
        super().__init__(name, description, found)
    
    def __str__(self):
        return "{} - {} \n======\nDamage: {}".format( self.name, self.description, self.damage)

class Food(Item):
    def __init__(self, name, description, found, value):
        self.value = value
        super().__init__(name, description, found)
    def __str__(self):
        return "{} - {} \n======\nFood Value: {}".format( self.name, self.description, self.value)

class Apple(Food):
    def __init__(self):
        self.found = False
        super().__init__(name="Rock", description="A simple weapon", found=False, value=5)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock", description="A simple weapon", found=True, damage=5)

class Pipe(Weapon):
    def __init__(self):
        self.found = False
        super().__init__(name="Pipe", description="A rusty pipe", found=False, damage=6)
