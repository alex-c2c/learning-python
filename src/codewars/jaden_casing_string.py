#!/usr/bin/env python

def to_jaden_case(string:str) -> str:
    char_list:list[str] = list(string)
    is_cap:bool = False

    for x in range(len(char_list)):
        if char_list[x] == ' ':
            is_cap = True;
            continue

        if is_cap or x is 0:
           char_list[x] = char_list[x].upper()
           is_cap = False
        else:
            char_list[x] = char_list[x].lower()

    return "".join(char_list)

if __name__ == "__main__":
    assert to_jaden_case("How can mirrors be real if our eyes aren't real") ==  "How Can Mirrors Be Real If Our Eyes Aren't Real"
