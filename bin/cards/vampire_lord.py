import being


class VampireLord(being.Being):
    stats = [
        {'manacost': 8,
         'attack': 7,
         'health': 7,
         'heal': 4},

        {'manacost': 7,
         'attack': 7,
         'health': 7,
         'heal': 5},

        {'manacost': 6,
         'attack': 7,
         'health': 7,
         'heal': 6},

        {'manacost': 5,
         'attack': 7,
         'health': 7,
         'heal': 7}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def effect(self, target, game):
        game.attack_being_triggers.append(self.heal_owner)
        game.attack_player_triggers.append(self.heal_owner)

    def heal_owner(self, a_being, game):
        if a_being[0] is self:
            game.heal(self.owner, self.stats[self.get_level()]['heal'])

    def kill(self, game):
        game.attack_being_triggers.remove(self.heal_owner)
        game.attack_player_triggers.remove(self.heal_owner)
