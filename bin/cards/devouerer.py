import being


class Devouerer(being.Being):
    stats = [
        {'manacost': 2,
         'attack': 4,
         'health': 4},

        {'manacost': 2,
         'attack': 5,
         'health': 4},

        {'manacost': 2,
         'attack': 5,
         'health': 5},

        {'manacost': 1,
         'attack': 5,
         'health': 5}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.NECROMANCER

    def pay_cost(self, payment, game):
        game.kill(payment)

    def cost_check(self, payment):
        if payment in self.owner.field:
            return True
        return False
