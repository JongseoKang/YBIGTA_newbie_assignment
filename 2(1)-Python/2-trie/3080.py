from lib import Trie
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