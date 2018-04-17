import enum
import card


class Being(card.Card):

    class Subtype(enum.Enum):
        WARRIOR = enum.auto()
        ROGUE = enum.auto()
        NECROMANCER = enum.auto()

    def __init__(self):
        super().__init__()
        self.has_attacked = True
        self.type = card.Card.Type.BEING

    def kill(self, game):
        pass
