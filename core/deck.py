def build_standard_deck() -> list[dict]:
    suite = "H", "C", "D", "S"
    rank = []
    for i in range(1,14):
        for j in suite:
            rank.append({"suite": j,"rank": i})
    return rank

def shuffle_by_suite(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in swaps:
        return deck

