import enum

experience_levels = [0, 100, 300, 600]


class Card:

    class Type(enum.Enum):
        BEING = enum.auto()
        ITEM = enum.auto()
        SPELL = enum.auto()

    stats = []
    text = ''

    def __init__(self):
        self.experience = 0
        self.type = None
        self.zone = None
        self.owner = None
        self.name = self.__class__.__name__

        self.update_stats()

    def info(self):
        card_info = dict()

        card_info['name'] = self.name
        card_info['text'] = self.text
        card_info['cost'] = self.get_manacost()
        card_info['experience'] = self.experience
        card_info['type'] = str(self.type)

        return card_info

    def get_stat(self, stat):
        return self.stats[self.get_level()][stat]

    def update_stats(self):
        for stat in self.stats[self.get_level()]:
            setattr(self, stat, self.stats[self.get_level()][stat])

    def cost_check(self, payment):
        return True

    def pay_cost(self, payment, game):
        return True

    def target_check(self, target):
        return True

    def set_zone(self, zone, game):
        self.zone = zone

    def effect(self, target, game):
        pass
        # getattr(self, '_effect_' + str(self.get_level()))(target, game)

    def get_level(self):
        for threshold in reversed(experience_levels):
            if self.experience >= threshold:
                return experience_levels.index(threshold)

    def get_manacost(self):
        return self.stats[self.get_level()]['manacost']

    def __str__(self):
        return self.name
