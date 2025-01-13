from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    size: int = 0
    pow_size: int = 1
    nodes:list[U] = []
    op: Callable[[U, U], U] = None
    def __init__(self, n: int, types: Generic[T, U]) -> None:
        self.size = n
        self.op = types[0]
        self.pow_size = 1
        while self.pow_size < n:
            self.pow_size *= 2
        self.nodes = [types[1]()] * (2 * self.pow_size) # node index starts from 1

    def update(self, i: int, x: U) -> None:
        i += self.pow_size - 1
        self.nodes[i] += x
        while i > 1:
            i //= 2
            self.nodes[i] = self.op(self.nodes[i * 2], self.nodes[i * 2 + 1])
    
    def query(self, l: int, r: int) -> U:
        l += self.pow_size - 1
        r += self.pow_size - 1
        ret = 0
        while l < r:
            if l % 2 == 1:
                ret = self.op(ret, self.nodes[l])
                l += 1
            if r % 2 == 0:
                ret = self.op(ret, self.nodes[r])
                r -= 1
            l //= 2
            r //= 2
        
        if l == r:
            ret = self.op(ret, self.nodes[l])
        return ret


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