import spell


class Resurrect(spell.Spell):

    stats = [
        {'manacost': 4},

        {'manacost': 3},

        {'manacost': 2},

        {'manacost': 1}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = spell.Spell.Subtype.NECROMANCY

    def effect(self, target, game):
        if self.target_check(target):
            game.resurrect(target)

    def target_check(self, target):
        if target in self.owner.grave:
            return True
        return False
