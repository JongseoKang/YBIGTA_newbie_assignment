from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000
    powers = {}

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        '''
        set value to matrix[key[0]][key[1]]
        '''
        # 구현하세요!
        self.matrix[key[0]][key[1]] = value % self.MOD

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        '''
        recursive matrix multiplication with memoization
        '''
        # 구현하세요!
        if n == 0:
            return self.eye(self.shape[0])
        elif n == 1:
            return self.clone()
        elif n in self.powers:
            return self.powers[n]
        elif n % 2 == 0:
            self.powers[n] = self.__pow__(int(n / 2)).__matmul__(self.__pow__(int(n / 2))) % self.MOD
            return self.powers[n]
        else:
            self.powers[n] = self.__pow__(int(n / 2)).__matmul__(self.__pow__(int(n / 2))).__matmul__(self.clone()) % self.MOD
            return self.powers[n]
    
    def __mod__(self, n: int) -> Matrix:
        '''
        mod matrix
        '''
        matrix = [[val % n for val in row] for row in self.matrix]
        return Matrix(matrix)

    def __repr__(self) -> str:
        '''
        matrix to string
        '''
        # 구현하세요!
        repr = ""
        for row in self.matrix:
            for val in row:
                repr += str(val % self.MOD) + " "
            repr += "\n"
        
        return repr


from typing import Callable
import sys


"""
아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()