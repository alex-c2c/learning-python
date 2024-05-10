#!/usr/bin/env python3

import re

def solve(original_string:str) -> str:
    if len(original_string) == 0:
        return ""

    stack:list[str] = []

    new_string = original_string.replace("[backspace]", "#")
    bs_list = re.findall(r"\#\*\d+", new_string)
    split_list = re.split(r"\#\*\d+", new_string)
    bs_index:int = 0

    for split_string in split_list:
        for s in split_string:
            if s == "#":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        if bs_index < len(bs_list):
            bs_count = int(bs_list[bs_index][2:])
            for _ in range(bs_count):
                if len(stack) > 0:
                    stack.pop()

        bs_index += 1

    return "".join(stack)


if __name__ == "__main__":
    assert solve("abcde[backspace]") == "abcd"
    assert solve("oopp[backspace]s") == "oops"
    assert solve("ooppp[backspace][backspace]s") == "oops"
    assert solve("[backspace]*1a") == "a"
    assert solve("ooppp[backspace]*2s") == "oops"
    assert solve("oop[backspace]*1oo[backspace]*2pppp[backspace]*3s") == "oops"
    assert solve("") == ""
    assert solve("[backspace]") == ""
    assert solve("[backspace]*3a  [backspace]") == "a "
    assert solve("No backspaces") == "No backspaces"
