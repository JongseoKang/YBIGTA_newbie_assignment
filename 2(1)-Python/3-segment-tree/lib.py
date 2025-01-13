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