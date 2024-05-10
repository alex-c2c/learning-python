#!/usr/bin/env python

def lottery(s:str) -> str:
    str_list:list[str] = [c for c in s if c.isdigit()]
    if len(str_list) == 0:
        return "One more run!"

    dedup_list = []
    for c in str_list:
        if c not in dedup_list:
            dedup_list.append(c)

    return "".join(dedup_list)

if __name__ == "__main__":
    assert lottery("wQ8Hy0y5m5oshQPeRCkG") == "805"
    assert lottery("ffaQtaRFKeGIIBIcSJtg") == "One more run!"
    assert lottery("555") == "5"
    assert lottery("HappyNewYear2020") == "20"
    assert lottery("20191224isXmas") == "20194"
    assert lottery("") == "One more run!"
