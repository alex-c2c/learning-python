#!/usr/bin/env python

def score(dice:list[int]) -> int:
    score_dict:dict[int, int] = {}

    for num in dice:
        if score_dict.get(num, None) is None:
            score_dict[num] = 1
        else:
            score_dict[num] += 1

    total_score:int = 0
    for i, k in enumerate(score_dict):
       total_score += get_score(k, score_dict[k]) 

    return total_score


def get_score(num:int, count:int) -> int:
    score:int = 0
    if num < 1 or num > 6:
        return score

    while count > 0:
        if num == 1:
            if count >= 3:
                score += 1000
                count -= 3
            elif count > 0 and count < 3:
                score += 100 * count
                count = 0
        elif num == 5:
            if count >= 3:
                score += 500
                count -= 3
            elif count > 0 and count < 3:
                score += 50 * count
                count = 0
        else:
            if count >= 3:
                score += num * 100
                count -= 3
            else:
                count = 0

    return score
   

if __name__ == "__main__":
    
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
