import importlib
import os


class Collection:

    def __init__(self):
        for card in os.listdir('bin/cards'):
            if card[0] != '_':
                setattr(self, card[:-3], importlib.import_module('cards.' + card[:-3]))

        self.deck = []
        self.c_deck = []

        # self.deck.append(getattr(self, 'barrier').Barrier())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'devouerer').Devouerer())
            self.c_deck.append(getattr(self, 'devouerer').Devouerer())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'death_stone').DeathStone())
            self.c_deck.append(getattr(self, 'death_stone').DeathStone())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'warlock').Warlock())
            self.c_deck.append(getattr(self, 'warlock').Warlock())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'necrotic_ooze').NecroticOoze())
            self.c_deck.append(getattr(self, 'necrotic_ooze').NecroticOoze())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'death_mage').DeathMage())
            self.c_deck.append(getattr(self, 'death_mage').DeathMage())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'entomb').Entomb())
            self.c_deck.append(getattr(self, 'entomb').Entomb())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'kill').Kill())
            self.c_deck.append(getattr(self, 'kill').Kill())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'life_drain').LifeDrain())
            self.c_deck.append(getattr(self, 'life_drain').LifeDrain())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'necro_stone').NecroStone())
            self.c_deck.append(getattr(self, 'necro_stone').NecroStone())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'necromancer').Necromancer())
            self.c_deck.append(getattr(self, 'necromancer').Necromancer())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'resurrect').Resurrect())
            self.c_deck.append(getattr(self, 'resurrect').Resurrect())

        for _ in range(0, 3):
            self.deck.append(getattr(self, 'shieldbearer').Shieldbearer())
            self.c_deck.append(getattr(self, 'shieldbearer').Shieldbearer())

        for _ in range(0, 1):
            self.deck.append(getattr(self, 'vampire_lord').VampireLord())
            self.c_deck.append(getattr(self, 'vampire_lord').VampireLord())

        print(len(self.deck))
