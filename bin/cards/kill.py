import card
import spell


class Kill(spell.Spell):

    stats = [
        {'manacost': 4},

        {'manacost': 3},

        {'manacost': 2},

        {'manacost': 1}
    ]

    text = 'Kill target being'

    def __init__(self):
        super().__init__()
        self.subtype = spell.Spell.Subtype.NECROMANCY

    def effect(self, target, game):
        if self.target_check(target):
            game.kill(target)

    def target_check(self, target):
        if target.type == card.Card.Type.BEING and (target in self.owner.field or target in self.owner.enemy.field):
            return True
        return False
