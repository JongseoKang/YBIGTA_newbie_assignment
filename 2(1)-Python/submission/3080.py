from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        current_index = 0 
        
        for elem in seq:
            found = False
            for child_index in self[current_index].children:
                if self[child_index].body == elem:
                    current_index = child_index  
                    found = True
                    break
            
            if not found:
                new_node = TrieNode(body=elem)
                new_index = len(self)
                self.append(new_node)
                self[current_index].children.append(new_index)  
                current_index = new_index 
        
        self[current_index].is_end = True

    # 구현하세요!


from typing import Callable
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
    lines: list[str] = sys.stdin.readlines()
    words = lines[1:]

    trie = Trie()
    result = 1
    for word in words:
        word = word.encode('ascii')
        trie.push(word)
    
    for node in trie:
        result *= facto(len(node.children) + node.is_end)
        result %= 1000000007
    
    print(result)

def facto(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f *= i
        f %= 1000000007
    return f


if __name__ == "__main__":
    main()