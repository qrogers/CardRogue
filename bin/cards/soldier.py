import being


class Soldier(being.Being):
    stats = [
        {'manacost': 2,
         'attack': 2,
         'health': 2},

        {'manacost': 2,
         'attack': 2,
         'health': 3},

        {'manacost': 2,
         'attack': 3,
         'health': 3},

        {'manacost': 1,
         'attack': 3,
         'health': 3}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = being.Being.Subtype.WARRIOR
