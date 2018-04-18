import card
import spell


class Fireball(spell.Spell):

    stats = [
        {'manacost': 3,
         'damage': 2},

        {'manacost': 2,
         'damage': 3},

        {'manacost': 2,
         'damage': 4},

        {'manacost': 1,
         'damage': 5}
    ]

    text = 'Deal {} damage to a being or player'

    def __init__(self):
        super().__init__()
        self.subtype = spell.Spell.Subtype.FIRE

    def info(self):
        card_info = super().info()
        card_info['text'] = self.text.format(self.get_stat('damage'))
        return card_info

    def effect(self, target, game):
        if self.target_check(target):
            game.deal_damage([(target, self.stats[self.get_level()]['damage'])])

    def target_check(self, target):
        if (target.type == card.Card.Type.BEING and (target in self.owner.field or target in self.owner.enemy.field))\
                or target.type == 'Player':
            return True
        return False
