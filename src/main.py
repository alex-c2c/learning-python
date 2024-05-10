#!/usr/bin/env python

from codewars.sum_of_dices import outcome2
from timing.timing import timeit

@timeit
def main() -> None:
    #print(f"outcome: {sum_of_dices.outcome(9, 9, 20)}")
    print(f"outcome2: {outcome2(10, 10, 20)}")


if __name__ == '__main__':
    main()
