import item


class Barrier(item.Item):

    stats = [
        {'manacost': 1},

        {'manacost': 1},

        {'manacost': 1},

        {'manacost': 0}
    ]

    text = 'Reduces all damage dealt to you by 1'

    def __init__(self):
        super().__init__()
        self.subtype = item.Item.Subtype.ENCHANTMENT

    def effect(self, target, game):
        game.damage_modifiers.append(self.reduce_by_one)
        game.destroy_triggers.append(self.destroy)

    def reduce_by_one(self, damage, target):
        if target.owner is self.owner and damage > 0:
            return damage - 1

    def destroy(self, game):
        game.damage_modifiers.remove(self.reduce_by_one)
