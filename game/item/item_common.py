from game.item.consumption.consumption_common import Consumption
from game.item.material.material_common import Material
from game.item.others.others_common import Others
from game.item.weapon.weapon_common import Weapon
from game.object.player_object.player_info import PlayerInfo


def add_item(item, info:PlayerInfo):
    print(item)
    if isinstance(item, Weapon):
        if item.name in info.item_dict['weapon']:
            info.item_dict['weapon'][item.name].append(item)
        else:
            info.item_dict['weapon'][item.name] = [item]
    elif isinstance(item, Consumption):
        if item.name in info.item_dict['consumption']:
            info.item_dict['consumption'][item.name] = (item, info.item_dict['consumption'][item.name][1] + 1)
        else:
            info.item_dict['consumption'][item.name] = (item, 1)
    elif isinstance(item, Material):
        if item.name in info.item_dict['material']:
            info.item_dict['material'][item.name] = (item, info.item_dict['material'][item.name][1] + 1)
        else:
            info.item_dict['material'][item.name] = (item, 1)
    elif isinstance(item, Others):
        if item.name in info.item_dict['others']:
            info.item_dict['others'][item.name] = (item, info.item_dict['others'][item.name][1] + 1)
        else:
            info.item_dict['others'][item.name] = (item, 1)
    else:
        pass

def use_item(item, info:PlayerInfo):
    can_use = False
    if isinstance(item, Weapon):
        if info.item_dict['weapon'][1] == 0:
            pass
        else:
            info.item_dict['weapon'][item.name] = (item, info.item_dict['weapon'][1] - 1)
            can_use = True
    elif isinstance(item, Consumption):
        if info.item_dict['consumption'][1] == 0:
            pass
        else:
            info.item_dict['consumption'][item.name] = (item, info.item_dict['consumption'][1] - 1)
            can_use = True
    elif isinstance(item, Material):
        if info.item_dict['material'][1] == 0:
            pass
        else:
            info.item_dict['material'][item.name] = (item, info.item_dict['material'][1] - 1)
            can_use = True
    elif isinstance(item, Others):
        if info.item_dict['others'][1] == 0:
            pass
        else:
            info.item_dict['others'][item.name] = (item, info.item_dict['others'][1] - 1)
            can_use = True
        pass

    return can_use
