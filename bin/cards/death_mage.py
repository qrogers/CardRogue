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

    text = 'Cast: Deal {} damage to your opponent'

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def info(self):
        card_info = super().info()
        card_info['text'] = self.text.format(self.get_stat('damage'))
        return card_info

    def effect(self, target, game):
        game.deal_damage([(game.get_other_player(self.owner), self.get_stat('damage'))])
