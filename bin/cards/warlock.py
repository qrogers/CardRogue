import being


class Warlock(being.Being):
    stats = [
        {'manacost': 2,
         'attack': 0,
         'health': 1},

        {'manacost': 2,
         'attack': 1,
         'health': 1},

        {'manacost': 1,
         'attack': 1,
         'health': 1},

        {'manacost': 1,
         'attack': 1,
         'health': 2}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def set_zone(self, zone, game):
        super().set_zone(zone, game)
        if zone is self.owner.field:
            game.draw(self.owner)
