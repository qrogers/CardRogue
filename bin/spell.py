import card
import enum


class Spell(card.Card):

    class Subtype(enum.Enum):
        FIRE = enum.auto()
        WATER = enum.auto()
        NECROMANCY = enum.auto()

    def __init__(self):
        super().__init__()
        self.type = card.Card.Type.SPELL
