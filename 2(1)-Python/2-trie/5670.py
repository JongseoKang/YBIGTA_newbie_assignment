from lib import Trie
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