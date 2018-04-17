import enum
import card


class Item(card.Card):

    class Subtype(enum.Enum):
        ARTIFACT = enum.auto()
        ENCHANTMENT = enum.auto()

    def __init__(self):
        super().__init__()
        self.type = card.Card.Type.ITEM

    def destroy(self, game):
        pass
