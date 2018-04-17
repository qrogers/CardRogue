import card
import player
import random


class Game:

    def __init__(self, h_deck, c_deck):
        self.h_deck = h_deck
        self.c_deck = c_deck

        for a_card in h_deck:
            a_card.zone = h_deck

        for a_card in c_deck:
            a_card.zone = c_deck

        self.draw_triggers = []
        self.mana_triggers = []
        self.cast_triggers = []
        self.damage_being_triggers = []
        self.damage_player_triggers = []
        self.heal_triggers = []
        self.attack_being_triggers = []
        self.attack_player_triggers = []
        self.kill_triggers = []
        self.destroy_triggers = []
        self.resurrect_triggers = []
        self.discard_triggers = []
        self.entomb_triggers = []
        self.end_triggers = []

        self.damage_modifiers = []

        self.h_hand = []
        self.c_hand = []

        self.h_field = []
        self.c_field = []

        self.h_inventory = []
        self.c_inventory = []

        self.h_grave = []
        self.c_grave = []

        self.h_manapool = []
        self.c_manapool = []

        self.h_player = player.Player(self.h_deck, self.h_hand, self.h_field, self.h_inventory, self.h_grave,
                                      self.h_manapool)
        self.c_player = player.Player(self.c_deck, self.c_hand, self.c_field, self.c_inventory, self.c_grave,
                                      self.c_manapool)

        self.h_player.set_enemy(self.c_player)
        self.c_player.set_enemy(self.h_player)

        for a_card in self.h_deck:
            a_card.owner = self.h_player
            # a_card.experience = 10000
            a_card.update_stats()

        for a_card in self.c_deck:
            a_card.owner = self.c_player
            # a_card.experience = 10000
            a_card.update_stats()

        self.turn_player = self.c_player

        self.shuffle(h_deck)
        self.shuffle(c_deck)

        self.draw(self.h_player)
        self.draw(self.h_player)
        self.draw(self.h_player)
        self.draw(self.h_player)

        self.draw(self.c_player)
        self.draw(self.c_player)
        self.draw(self.c_player)
        self.draw(self.c_player)

        self.end()

    @staticmethod
    def shuffle(deck):
        random.shuffle(deck)

    def add_mana(self, a_card):
        if not a_card.owner.mana_per_turn:
            a_card.owner.mana_per_turn = True
            self.turn_player.hand.remove(a_card)
            self.turn_player.manapool.append(a_card)
            self.turn_player.mana += 1
            a_card.set_zone(self.turn_player.manapool, self)
            self._trigger('mana', a_card)

    def attack_being(self, a_being, d_being):
        if not a_being.has_attacked:
            a_being.has_attacked = True
            self.deal_damage([(d_being, a_being.attack), (a_being, d_being.attack)])
            self._trigger('attack_being', [a_being, d_being])

    def attack_player(self, a_being, d_player):
        if not a_being.has_attacked:
            a_being.has_attacked = True
            self.deal_damage([(d_player, a_being.attack)])
            self._trigger('attack_player', [a_being, d_player])

    def activate(self, a_item, target):
        a_item.activate(target, self)
        # trigger

    def end(self):
        self._trigger('end', self.turn_player)

        self.turn_player = self.get_other_player(self.turn_player)

        for a_being in self.turn_player.field:
            a_being.has_attacked = False
        self.turn_player.mana_per_turn = False
        self.turn_player.mana = len(self.turn_player.manapool)
        self.draw(self.turn_player)

    def cast(self, a_card, target=None, cost=None):
        if a_card.manacost <= a_card.owner.mana and a_card.cost_check(cost):
            a_card.owner.mana -= a_card.manacost
            a_card.pay_cost(cost, self)
            a_card.zone.remove(a_card)
            if a_card.type is card.Card.Type.SPELL:
                a_card.effect(target, self)
                a_card.owner.grave.append(a_card)
                a_card.set_zone(a_card.owner.grave, self)
            elif a_card.type is card.Card.Type.BEING:
                a_card.effect(target, self)
                a_card.owner.field.append(a_card)
                a_card.set_zone(a_card.owner.field, self)
            elif a_card.type is card.Card.Type.ITEM:
                a_card.effect(target, self)
                a_card.owner.inventory.append(a_card)
                a_card.set_zone(a_card.owner.inventory, self)

            self._trigger('cast', [a_card, target])

    def deal_damage(self, instances):
        for instance in instances:
            target = instance[0]
            damage = instance[1]
            damage = self._modify_damage(damage, target)
            target.health -= damage
        for instance in instances:
            target = instance[0]
            damage = instance[1]
            if target.type == 'Player':
                self._trigger('damage_player', [target, damage])
            elif target.type is card.Card.Type.BEING:
                self._trigger('damage_being', [target, damage])
            else:
                raise Exception('UNKNOWN_TYPE')
        for instance in instances:
            target = instance[0]
            if type(target).__base__.__name__ == 'Being':
                if target.health <= 0:
                    self.kill(target)

    def heal(self, target, amount):
        if type(target).__name__ == 'Player':
            target.health += amount
        elif type(target).__base__.__name__ == 'Being':
            if target.health < target.stats[target.get_level()]['health']:
                target.health += amount
        else:
            raise Exception('UNKNOWN_TYPE')
        self._trigger('heal', [target, amount])

    def _modify_damage(self, damage, target):
        for modifier in self.damage_modifiers:
            damage = modifier(damage, target)
        return damage

    def draw(self, a_player):
        if len(a_player.deck) > 0:
            drawn_card = a_player.deck.pop()
            if len(a_player.hand) < 8:
                a_player.hand.append(drawn_card)
                drawn_card.set_zone(a_player.hand, self)
            else:
                a_player.grave.append(drawn_card)
                drawn_card.set_zone(a_player.grave, self)
            self._trigger('draw', drawn_card)

    def kill(self, a_being):
        a_being.owner.field.remove(a_being)
        a_being.owner.grave.append(a_being)
        a_being.set_zone(a_being.owner.grave, self)
        a_being.kill(self)
        self._trigger('kill', a_being)

    def destroy(self, a_item):
        a_item.owner.inventory.remove(a_item)
        a_item.owner.grave.append(a_item)
        a_item.set_zone(a_item.owner.grave, self)
        a_item.destroy(self)
        self._trigger('destroy', a_item)

    def discard(self, a_card):
        a_card.owner.hand.remove(a_card)
        a_card.owner.grave.append(a_card)
        a_card.set_zone(a_card.owner.grave, self)
        self._trigger('discard', a_card)

    def resurrect(self, a_being):
        a_being.owner.grave.remove(a_being)
        a_being.owner.field.append(a_being)
        a_being.set_zone(a_being.owner.field, self)
        self._trigger('resurrect', a_being)

    def entomb(self, a_card):
        a_card.owner.deck.remove(a_card)
        a_card.owner.grave.append(a_card)
        a_card.set_zone(a_card.owner.grave, self)
        self._trigger('entomb', a_card)

    def _trigger(self, trig, cause):
        for trigger in getattr(self, trig + '_triggers'):
            trigger(cause, self)

    def get_other_player(self, a_player):
        if a_player is self.h_player:
            return self.c_player
        elif a_player is self.c_player:
            return self.h_player
        else:
            raise Exception("INVALID PLAYER")
