#!/usr/bin/env python

def on_line(points:tuple[tuple[int, int],...]) -> bool:
    if len(points) <= 2:
        return True

    for index in range(len(points)):
        x1, y1 = points[index]
        x2, y2 = points[index+1]
        x3, y3 = points[index+2]

        if (y1 - y2) * (x1 - x3) != (y1 - y3) * (x1 - x2):
            return False

        if index == len(points) - 3:
            break

    return True

if __name__ == "__main__":
    assert on_line(((1,2), (7,4), (22,9))) == True
    assert on_line(((1,2), (7,4), (22,8))) == False
    assert on_line(((7,4), (1,2), (22,9))) == True
    assert on_line(((1,2), (-3,-14), (22,9))) == False
    assert on_line(((1,2), (-3,14))) == True
    assert on_line(((-1,-4), (-2,-8), (-3,-12))) == True
    assert on_line(((5,10), (6,12), (7,14), (10,20), (23,46), (17,34))) == True
    assert on_line(((5,10), (6,12), (7,14), (10,20), (23,46), (17,35))) == False
    assert on_line(((3,4), (5,6), (67,54), (3,19), (90,5))) == False
    assert on_line(((2,1), (4,1), (7,1))) == True
    assert on_line(((1,2), (1,4), (1,7))) == True
    assert on_line(((1,1), (0,0), (1,-1))) == False
    assert on_line(()) == True
    assert on_line(((1,1),)) == True
    assert on_line(((1,1), (1,1))) == True
    assert on_line(((1,4), (1,4), (3,4), (17,4), (34,4))) == True
    assert on_line(((1,4), (1,4), (3,4), (3,4), (17,4), (17,4), (34,4), (34,4))) == True
    assert on_line(((1,1), (1,1), (0,0), (1,-1))) == False
