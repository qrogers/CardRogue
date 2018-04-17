import being


class Shieldbearer(being.Being):
    stats = [
        {'manacost': 3,
         'attack': 0,
         'health': 4},

        {'manacost': 3,
         'attack': 0,
         'health': 5},

        {'manacost': 2,
         'attack': 0,
         'health': 5},

        {'manacost': 2,
         'attack': 0,
         'health': 6}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def effect(self, target, game):
        game.end_triggers.append(self.heal_self)

    def kill(self, game):
        game.end_triggers.remove(self.heal_self)

    def heal_self(self, player, game):
        if player is not self.owner:
            game.heal(self, 1)
