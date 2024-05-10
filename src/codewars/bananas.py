#!/urs/bin/env python

def bananas(s:str) -> set[str]:
    if len(s) < 6:
        return set()

    bananas_list = []

    return set()

if __name__ == "__main__":
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a", "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a", "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
