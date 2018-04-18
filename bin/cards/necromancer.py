import being


class Necromancer(being.Being):
    stats = [
        {'manacost': 6,
         'attack': 1,
         'health': 3},

        {'manacost': 6,
         'attack': 2,
         'health': 3},

        {'manacost': 5,
         'attack': 2,
         'health': 3},

        {'manacost': 4,
         'attack': 2,
         'health': 3}
    ]

    text = 'Cast: Resurrect a being in your grave'

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def effect(self, target, game):
        if self.target_check(target):
            game.resurrect(target)

    def target_check(self, target):
        if target in self.owner.grave:
            return True
        return False
