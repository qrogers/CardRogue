class Player:

    def __init__(self, deck, hand, field, inventory, grave, manapool):
        self.deck = deck
        self.hand = hand
        self.field = field
        self.inventory = inventory
        self.grave = grave
        self.manapool = manapool + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.owner = self
        self.enemy = None

        self.type = 'Player'

        self.health = 25
        self.mana = 0

        self.mana_per_turn = False

    def set_enemy(self, enemy):
        self.enemy = enemy
