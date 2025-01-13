from lib import SegmentTree
from typing import Callable
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""

def main() -> None:
    # 구현하세요!
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]
    lines: list[str] = sys.stdin.readlines()
    n = intify(lines[0])[0]
    queries = [intify(line) for line in lines[1:]]

    sum = lambda a, b: a + b
    segTree = SegmentTree(1000000, [sum, int]) # gen segTree with 0s
    for query in queries:
        if query[0] == 1:
            candy = find(segTree, query[1])
            segTree.update(candy, -1)
            print(candy)
        else:
            segTree.update(query[1], query[2])

def find(segTree: SegmentTree, rank: int):
    l = 1
    r = segTree.pow_size - 1

    while l < r:
        mid = (l + r) // 2
        sum = segTree.query(1, mid)
        if l == r - 1:
            if sum >= rank:
                return l
            else:
                return r
        elif sum >= rank:
            r = mid
        elif sum < rank:
            l = mid
    
    return l

if __name__ == "__main__":
    main()