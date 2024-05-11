#!usr/bin/env python3

from dataclasses import dataclass, field
#from linkedlist.linkedlist2 import LinkedList, LinkedListNode, Test
from linkedlist.linkedlist import LinkedList, LinkedListNode

def generate_id() -> str:
    return ""

@dataclass(frozen=False)
class Coin:
    id:str = field(init=False, default_factory=generate_id)
    position:tuple[int, int] = (0,0)
    some_list:list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        pass


def main() -> None:
    ll = LinkedList(None)

    for x in range(10):
        ll.add_value_tail(x)

    ll.print_all_elements()

    ll.insert_value(100, 2)
    ll.insert_value_reverse(200, 2)

    ll.print_all_elements()

if __name__ == "__main__":
    main()
