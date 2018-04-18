import card
import spell


class Entomb(spell.Spell):

    stats = [
        {'manacost': 4},

        {'manacost': 3},

        {'manacost': 2},

        {'manacost': 1}
    ]

    text = 'Put a being in your deck into your grave'

    def __init__(self):
        super().__init__()
        self.subtype = spell.Spell.Subtype.NECROMANCY

    def effect(self, target, game):
        if self.target_check(target):
            game.entomb(target)

    def target_check(self, target):
        if target in self.owner.deck and target.type is card.Card.Type.BEING:
            return True
        return False
