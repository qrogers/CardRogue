import being


class DeathMage(being.Being):
    stats = [
        {'manacost': 3,
         'attack': 2,
         'health': 1,
         'damage': 2},

        {'manacost': 3,
         'attack': 2,
         'health': 2,
         'damage': 2},

        {'manacost': 2,
         'attack': 2,
         'health': 2,
         'damage': 2},

        {'manacost': 2,
         'attack': 2,
         'health': 2,
         'damage': 3}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def effect(self, target, game):
        game.deal_damage([(game.get_other_player(self.owner), self.stats[self.get_level()]['damage'])])
