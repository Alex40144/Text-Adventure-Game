import world, inspect
from player import Player


def play():
    player = Player()
    room = world.get_tile("StartingRoom")
    player.tile = room
    room = room()
    while player.is_alive() and not player.victory:
        room = player.current_tile()
        room = room()
        room.modify_player(player)
        print(inspect.cleandoc(room.intro_text()))
        if player.is_alive() and not player.victory:
            print("\n===========================================\nChoose an action:")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('\nAction: ')
            print("\n===========================================\n")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                else:
                    print("That wasn't an avaliable action.\n")


if __name__ == "__main__":
    play()