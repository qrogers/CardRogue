import item


class DeathStone(item.Item):

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

    text = 'Charge: Whenever a being dies' \
           'Activate 2: Resurrect target being in your grave'

    def __init__(self):
        super().__init__()
        self.subtype = item.Item.Subtype.ARTIFACT
        self.charges = 0

    def effect(self, target, game):
        game.kill_triggers.append(self.gain_charge)

    def gain_charge(self, a_being, game):
        self.charges += 1

    def activate(self, target, game):
        if self.charges >= 2 and self.target_check(target):
            game.destroy(self)
            game.resurrect(target)
            game.kill_triggers.remove(self.gain_charge)

    def destroy(self, game):
        game.kill_triggers.remove(self.gain_charge)

    def target_check(self, target):
        if target in self.owner.grave:
            return True
        return False
