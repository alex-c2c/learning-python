#!/usr/bin/env python

def ip_to_int32(ip:str) -> int:
    octet_list:list[str] = ip.split(".")
    int_list:list[int]= [int(octet) for octet in octet_list]
    bin_list:list[str] = [bin(i)[2:].zfill(8) for i in int_list]
    bin_str:str = "".join(bin_list)
    bin_int:int = int(bin_str, 2)

    return bin_int

if __name__ == "__main__":
    assert ip_to_int32("128.114.17.104") == 2154959208
    assert ip_to_int32("0.0.0.0") == 0
    assert ip_to_int32("128.32.10.1") == 2149583361
    
#['10000000', '1110010', '10001', '1101000']

