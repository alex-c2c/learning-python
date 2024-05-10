#!/usr/bin/env python3

def clean_string(s:str) -> str:
    if len(s) == 0:
        return ""

    s_list = list(s)
    index:int = 0
    while True:
        if s_list[index] == "#":
            s_list.pop(index)
            if index > 0:
                s_list.pop(index - 1)
                index -= 1

        else:
            index += 1
        if index >= len(s_list):
            break

    return "".join(s_list) 

if __name__ == "__main__":
    assert clean_string("abc#d##c") == "ac"
    assert clean_string("abc####d##c#") == ""
    assert clean_string("#######") == ""
    assert clean_string("") == ""
    assert clean_string("L###{_#wO##L!") == "{L!"

