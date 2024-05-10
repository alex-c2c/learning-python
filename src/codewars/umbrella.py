#!/usr/bin/env python3

def min_umbrella(weather_list: list[str]) -> int:
    home_umbrella_count:int = 0
    work_umbrella_count:int = 0

    counter:int = 0
    while counter < len(weather_list):
        if weather_list[counter] == "rainy" or weather_list[counter] == "thunderstorm":
            if counter % 2 == 0: # home -> work
                if home_umbrella_count > 0:
                    home_umbrella_count -= 1
                    work_umbrella_count += 1
                else:
                    work_umbrella_count += 1
            else: # work -> home
                if work_umbrella_count > 0:
                    work_umbrella_count -= 1
                    home_umbrella_count += 1
                else:
                    home_umbrella_count += 1
        else:
            pass

        counter += 1
    
    return home_umbrella_count + work_umbrella_count


if __name__ == '__main__':
    assert min_umbrella(["cloudy"]) == 0
    assert min_umbrella(["rainy", "rainy", "rainy", "rainy"]) == 1
    assert min_umbrella(["overcast", "rainy", "clear", "thunderstorm"]) == 2
