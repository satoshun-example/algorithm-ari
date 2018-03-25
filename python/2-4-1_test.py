#!/usr/local/bin/python3


class HeapTree:
    def __init__(self, l):
        self.data = []
        for i in l:
            self.add(i)

    def pop(self):
        p = self.data[0]
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]
        self._sort_head(0)
        return p

    def add(self, v):
        self.data += [v]
        self._sort_tail()

    def _sort_head(self, head):
        left = head * 2
        right = head * 2 + 1
        try:
            if self.data[left] < self.data[head]:
                self.data[left], self.data[head] = \
                        self.data[head], self.data[left]
                self._sort_head(left)
        except IndexError:
            pass
        try:
            if self.data[right] < self.data[head]:
                self.data[right], self.data[head] = \
                        self.data[head], self.data[right]
                self._sort_head(right)
        except IndexError:
            pass

    def _sort_tail(self):
        last = len(self.data) - 1
        while True:
            if last == 0:
                return
            parent = round(last / 2)
            if self.data[parent] > self.data[last]:
                self.data[parent], self.data[last] = \
                        self.data[last], self.data[parent]
            else:
                break
            last = parent


## 2分木 heap
def createHeapTree(l):
    return HeapTree(l)


def test_heap():
    heap = createHeapTree([3, 1, 2, 10, 5, 100, 8, 24, 22, 6])
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 5
