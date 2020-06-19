import world
from player import Player


def play():
    world.load_tiles()
    player = Player()
    while player.is_alive and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive and not player.victory: #check again as room could of changed player's state
            print("Choose an action:\n")
            availiable_actions = room.availiable_actions()
            for action in availiable_actions:
                print(action)
            action_input = input('Action: ')
            for action in availiable_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()