#!/usr/bin/env python3

def bomb_has_been_planted(m:list, time:int) -> bool:
    pos_dict:dict[str, tuple[int, int]] = get_all_pos(m) 

    if pos_dict.get("B", None) is None:
        return True

    if pos_dict.get("CT", None) is None:
        return False
        
    scenario_dict = {}
    if pos_dict.get("K", None) is not None:
        scenario_dict["use_kit"] = get_step_count(pos_dict["CT"], pos_dict["K"]) + get_step_count(pos_dict["K"], pos_dict["B"]) + 5
    
    scenario_dict["skip_kit"] = get_step_count(pos_dict["CT"], pos_dict["B"]) + 10

    is_in_time:bool = False
    for k in scenario_dict.keys():
        if scenario_dict[k] <= time:
            is_in_time = True
            break

    return is_in_time


def get_all_pos(m:list[list[str]]) -> dict[str, tuple[int, int]]:
    pos_dict = {}

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "K":
                pos_dict["K"] = (x, y)
            elif m[y][x] == "CT":
                pos_dict["CT"] = (x, y)
            elif m[y][x] == "B":
                pos_dict["B"] = (x, y)

    return pos_dict

def get_step_count(source:tuple[int, int], dest:tuple[int, int]) -> int:
    current_x:int = source[0]
    current_y:int = source[1]
    step_count:int = 0

    while True:
        if current_x == dest[0] and current_y == dest[1]:
            break

        if current_x < dest[0]:
            current_x += 1
        elif current_x > dest[0]:
            current_x -= 1

        if current_y < dest[1]:
            current_y += 1
        elif current_y > dest[1]:
            current_y -= 1

        step_count += 1

    return step_count
        
                
if __name__ == "__main__":
    map1 = [
            ["CT", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "B"]
        ]

    assert bomb_has_been_planted(map1, 7) == False

    map3 = [
            ["CT", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "B", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]

    assert bomb_has_been_planted(map3, 13) == True

    map4 = [
            ["0", "0", "0", "CT"],
            ["0", "0", "0", "0"],
            ["B", "0", "0", "0"]
        ]

    assert bomb_has_been_planted(map4, 13) == True

    map5 = [
            ["0", "0", "0", "0", "0", "0"],
            ["CT", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "B"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "K", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"]
        ]

    assert bomb_has_been_planted(map5, 13) == True

    map6 = [
            ["0", "K", "0", "CT"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["B", "0", "0", "0"]
        ]

    assert bomb_has_been_planted(map6, 12) == True
