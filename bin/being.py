import enum
import card


class Being(card.Card):

    class Subtype(enum.Enum):
        WARRIOR = enum.auto()
        ROGUE = enum.auto()
        NECROMANCER = enum.auto()

    def __init__(self):
        super().__init__()
        self.attack = -1
        self.health = -1
        self.has_attacked = True
        self.type = card.Card.Type.BEING

    def info(self):
        card_info = super().info()

        card_info['attack'] = self.attack
        card_info['health'] = self.health

        return card_info

    def kill(self, game):
        pass
