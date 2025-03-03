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


import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        ### TODO
        new_index = None 
        for child_index in trie[pointer].children:
            if trie[child_index].body == element:
                new_index = child_index  
                break
        pointer = new_index


    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    # 구현하세요!
    while True:
        n, words = input_data()
        if n == -1:
            break
        trie = Trie()
        result = 0

        for word in words:
            trie.push(word)
        
        for word in words:
            result += count(trie, word)
        print(f"{(result / n):.2f}")

def input_data():
    '''
    get inputs from stdin
    '''
    try:
        n = int(input())
        words = [input().strip() for _ in range(n)]
        words = [word.encode('ascii') for word in words]
        return n,words
    except:
        return -1,[]

if __name__ == "__main__":
    main()