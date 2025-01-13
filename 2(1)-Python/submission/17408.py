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


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()