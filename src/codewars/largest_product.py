#!/usr/bin/env python3

def greatest_product(st:str) -> int:
    int_tuple:tuple[int, ...] = tuple(int(d) for d in st)

    highest_product:int = 0
    index:int = 0
    while True:
        if index > len(int_tuple) - 5:
            break

        sub_tuple = int_tuple[index:index + 5]
        product = get_combi_product(sub_tuple)
        if product > highest_product:
            highest_product = product

        index += 1

    return highest_product

def get_combi_product(sub_tuple:tuple[int, ...]) -> int:
    product:int = 1
    for n in sub_tuple:
        product *= n

    return product

if __name__ == "__main__":
    assert greatest_product("123834539327238239583") == 3240
    assert greatest_product("395831238345393272382") == 3240
    assert greatest_product("92494737828244222221111111532909999") == 5292
    assert greatest_product("92494737828244222221111111532909999") == 5292
    assert greatest_product("02494037820244202221011110532909999") == 0
    print(f"No assertion!")
