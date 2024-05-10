#!/usr/bin/env python3

import itertools

# optimize answer :)
def outcome2(n, s, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for x in range(1, min(s, j) + 1):
                dp[i][j] += dp[i - 1][j - x]
    
    return dp[n][k]

# my answer :(
def outcome(n:int, s:int, k:int) -> int:
    if k == 0:
        return 1

    if k < n or k > n * s:
        return 0

    count:int = 0
    a = [i for i in range(1, s + 1)]
    b = tuple(a)
    c = ((b,) * n)

    for t in product(c):
        if len(t) == n:
            sum:int = 0
            for num in t:
                sum += num

            if sum == k:
                count += 1

    return count

def product(dice_tuple:tuple[tuple[int, ...], ...]):
    if not dice_tuple:
        yield ()
    else:
        for d in dice_tuple[0]:
            for prod in product(dice_tuple[1:]):
                yield (d,)+prod

if __name__ == "__main__":
    #print(f"outcome = {outcome(2, 6, 2)}")
    outcome(8, 8, 60) 
    '''
    #outcome(2, 6, 10)
    assert outcome(8, 8, 80) == 0
    assert outcome(0, 6, 0) == 1
    assert outcome(0, 6, 1) == 0
    assert outcome(1, 6, 0) == 1
    assert outcome(1, 6, 1) == 1
    assert outcome(1, 6, 2) == 1
    assert outcome(1, 6, 3) == 1
    assert outcome(1, 6, 4) == 1
    assert outcome(1, 6, 5) == 1
    assert outcome(1, 6, 6) == 1
    assert outcome(1, 6, 7) == 0
    assert outcome(2, 6, 0) == 1
    assert outcome(2, 6, 1) == 0
    assert outcome(2, 6, 2) == 1
    assert outcome(2, 6, 3) == 2
    assert outcome(2, 6, 4) == 3
    assert outcome(2, 6, 5) == 4
    assert outcome(2, 6, 6) == 5
    assert outcome(2, 6, 7) == 6
    assert outcome(2, 6, 8) == 5
    assert outcome(2, 6, 9) == 4
    assert outcome(2, 6, 10) == 3
    assert outcome(2, 6, 11) == 2
    assert outcome(2, 6, 12) == 1
    assert outcome(2, 6, 13) == 0
    assert outcome(3, 6, 0) == 1
    assert outcome(3, 6, 6) == 10
    assert outcome(3, 6, 9) == 25
    assert outcome(3, 6, 10) == 27
    assert outcome(3, 6, 11) == 27
    assert outcome(3, 6, 12) == 25
    assert outcome(3, 6, 15) == 10
    assert outcome(4, 6, 0) == 1
    assert outcome(4, 6, 5) == 4
    '''
    print(f"finished all test successfully")
