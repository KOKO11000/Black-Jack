from deck import * 
from player_io import *
def calculate_hand_value(hand: list[dict]) -> int:
    for num in hand["rank"]:
        num = num
        J,Q,K = 10
        A = 1
    sum_hand = sum(hand)
    return sum_hand
    

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    pop_card = deck.pop()
    player = {pop_card, pop_card} 
    dealer = {pop_card,pop_card} 
    calculate_hand_value(player)
    calculate_hand_value(dealer)
    return player, dealer
    

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    if dealer > 21:
        return False
    if dealer > 17 or dealer < 21:
        return True
    else:
        return deck



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(build_standard_deck(),player, dealer)

    ask_player_action()
    