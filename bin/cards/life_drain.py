import spell


class LifeDrain(spell.Spell):

    stats = [
        {'manacost': 4},

        {'manacost': 3},

        {'manacost': 2},

        {'manacost': 1}
    ]

    text = 'Cost: Discard a card' \
           'Draw a card and deal 3 damage to your opponent'

    def __init__(self):
        super().__init__()
        self.subtype = spell.Spell.Subtype.NECROMANCY

    def pay_cost(self, payment, game):
        game.discard(payment)

    def cost_check(self, payment):
        if payment in self.owner.hand:
            return True
        return False

    def effect(self, target, game):
        game.draw(self.owner)
        game.deal_damage([(self.owner.enemy, 3)])
