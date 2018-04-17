class AI:

    def __init__(self):
        pass

    @staticmethod
    def take_action(game):
        if not game.c_player.mana_per_turn and len(game.c_player.manapool) < 6:
            if len(game.c_player.hand) > 0:
                game.add_mana(game.c_player.hand[0])
        for card in game.c_player.hand:
            if card.manacost <= game.c_player.mana:
                if len(game.h_field) > 0:
                    game.cast(card, game.h_field[0])
                else:
                    game.cast(card, game.h_player)
        for card in game.c_field:
            game.attack_player(card, game.h_player)
        game.end()
