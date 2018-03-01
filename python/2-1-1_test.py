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
