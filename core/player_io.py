def ask_player_action() -> str:
    user_choice = input("S or H: ")
    while True:
        if not user_choice.upper() == "H" or not user_choice.upper() == "S":
            return input("S or H: ")
        else:
           return user_choice.upper()
              