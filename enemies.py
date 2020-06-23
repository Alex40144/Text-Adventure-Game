#base class for all ingame enemies

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Person(Enemy):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

class Bob(Person):
    def __init__(self):
        super().__init__(name="Bob", hp = 40, damage=5)

class Bert(Person):
    def __init__(self):
        super().__init__(name="Bert", hp=10, damage = 2)