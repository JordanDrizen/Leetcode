from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.array_size = n
        self.arr = [None] * self.array_size
        self.ptr = 0
        self.returned = []

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        if idKey - 1 != self.ptr:
            return []
        else:
            if None in self.arr:
                end = self.arr.index(None)
            else:
                end = None
            self.ptr = end
            return self.arr[idKey - 1 : end]


solution = OrderedStream(5)
print(solution.insert(3, "cccc"))
print(solution.insert(1, "aaaaa"))
print(solution.insert(2, "bbbbb"))
print(solution.insert(5, "eeeee"))
print(solution.insert(4, "ddddd"))
