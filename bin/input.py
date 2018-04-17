import ai
import collection
import copy
import game


class Input:

    def __init__(self):
        self.h_collection = collection.Collection()
        h_deck = copy.deepcopy(self.h_collection.deck)
        c_deck = copy.deepcopy(self.h_collection.c_deck)
        self.a_game = game.Game(h_deck, c_deck)

        self.ai = ai.AI()

        print(self.a_game.h_player.field)

        while True:
            self.draw_game()
            if self.a_game.turn_player is self.a_game.h_player:
                self._handle_input(input())
            elif self.a_game.turn_player is self.a_game.c_player:
                self.ai.take_action(self.a_game)
            else:
                raise Exception("UNKNOWN_PLAYER")

    def draw_game(self):
        print('Health: ' + str(self.a_game.c_player.health) + ' Mana: ' + str(self.a_game.c_player.mana) + '/' + str(len(self.a_game.c_manapool)))
        print('Cards: ' + str(len(self.a_game.c_hand)))
        print('----------')
        beings = ''
        for card in self.a_game.c_field:
            beings += str(card.attack) + str(card)[:1] + str(card.health) + ' '
        print(beings)
        print()
        beings = ''
        for card in self.a_game.h_field:
                beings += str(card.attack) + str(card)[:1] + str(card.health) + ' '
        print(beings)
        print('----------')
        items = ''
        for card in self.a_game.h_inventory:
                items += str(card)[:1]
        print(items)
        print('----------')
        print('Health: ' + str(self.a_game.h_player.health) + ' Mana: ' + str(self.a_game.h_player.mana) + '/' + str(len(self.a_game.h_manapool)))
        print(','.join(str(card) for card in self.a_game.h_player.hand))

    def _handle_input(self, command):
        try:
            if command != '':
                inputs = command.split(' ')
                if inputs[0] == 'm':
                    self.a_game.add_mana(self.a_game.h_hand[int(inputs[1])])
                elif inputs[0] == 'c':
                    target = None
                    cost = None
                    if len(inputs) >= 3:
                        if inputs[2] == 'h':
                            target = self.a_game.h_player
                        elif inputs[2] == 'c':
                            target = self.a_game.c_player
                        elif inputs[2] == 'g':
                            target = self.a_game.h_grave[int(inputs[3])]
                        elif inputs[2] == 'ph':
                            cost = self.a_game.h_hand[int(inputs[3])]
                        elif inputs[2] == 'pf':
                            cost = self.a_game.h_field[int(inputs[3])]
                        elif inputs[2] == 'd':
                            for card in self.a_game.h_deck:
                                if card.name == inputs[3]:
                                    target = card
                                    break
                        else:
                            target = self.a_game.c_field[int(inputs[2])]
                    self.a_game.cast(self.a_game.h_hand[int(inputs[1])], target, cost)
                elif inputs[0] == 'x':
                    self.a_game.activate(self.a_game.h_inventory[int(inputs[1])], self.a_game.h_grave[int(inputs[2])])
                elif inputs[0] == 'a':
                    if len(inputs) == 3:
                        self.a_game.attack_being(self.a_game.h_field[int(inputs[1])],
                                                 self.a_game.c_field[int(inputs[2])])
                    else:
                        self.a_game.attack_player(self.a_game.h_field[int(inputs[1])], self.a_game.c_player)
                elif inputs[0] == 'e':
                    self.a_game.end()
        except Exception as e:
            raise e
