import being


class NecroticOoze(being.Being):
    stats = [
        {'manacost': 2,
         'attack': 1,
         'health': 1,
         'heal': 2},

        {'manacost': 2,
         'attack': 1,
         'health': 2,
         'heal': 2},

        {'manacost': 2,
         'attack': 2,
         'health': 2,
         'heal': 2},

        {'manacost': 1,
         'attack': 2,
         'health': 2,
         'heal': 2}
    ]

    text = 'Death: You gain {} health'

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def info(self):
        card_info = super().info()
        card_info['text'] = self.text.format(self.get_stat('heal'))
        return card_info

    def kill(self, game):
        game.heal(self.owner, self.get_stat('heal'))
