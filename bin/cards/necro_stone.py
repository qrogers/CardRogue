import item


class NecroStone(item.Item):

    stats = [
        {'manacost': 2,
         'damage': 2},

        {'manacost': 2,
         'damage': 3},

        {'manacost': 1,
         'damage': 3},

        {'manacost': 1,
         'damage': 4}
    ]

    def __init__(self):
        super().__init__()
        self.subtype = item.Item.Subtype.ARTIFACT

    def effect(self, target, game):
        game.resurrect_triggers.append(self.necro_damage)

    def necro_damage(self, a_being, game):
        if a_being.owner is self.owner:
            game.deal_damage([(self.owner.enemy, self.stats[self.get_level()]['damage'])])

    def destroy(self, game):
        game.resurrect_triggers.remove(self.necro_damage)
