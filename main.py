from core import *
from core.deck import *
from core.game_logic import *
from core.player_io import *
if __name__ == "__main__":
    build_standard_deck()
    shuffle_by_suite(build_standard_deck())

    player = {"hand": []}
    dealer = {"hand": []}

    run_full_game(build_standard_deck(), player, dealer)
