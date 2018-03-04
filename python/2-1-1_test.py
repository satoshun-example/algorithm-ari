#!/usr/local/bin/python3

## 階乗
def test_fact():
    def fact(n) -> int:
        if n == 1:
            return 1
        return n * fact(n - 1)
    assert fact(10) == 3628800

## フィボナッチ数
def test_fib():
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    assert fib(10) == 55

## フィボナッチ数 + キャッシュ
def test_fib_cache():
    cache = dict()
    def fib(n):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]
    assert fib(10) == 55

## スタック
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack:
    head = None

    def push(self, value):
        head = Node(value, self.head)
        self.head = head

    def pop(self):
        p = self.head
        if p is not None:
            self.head = p.next
            return p.value
        return None

def test_stack():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(50)
    assert stack.pop() == 50
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() is None


## キュー
class Queue:
    head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = Node(value, None)

    def pop(self):
        if self.head is None:
            return None
        head = self.head
        self.head = head.next
        return head.value

def test_queue():
    queue = Queue()
    queue.push(10)
    queue.push(20)
    queue.push(50)
    assert queue.pop() == 10
    assert queue.pop() == 20
    assert queue.pop() == 50
    assert queue.pop() is None
