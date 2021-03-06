package com.github.satoshun.example.algorithm.ari

fun fibonacci(n: Int): Int {
  fun _fibonacci(n: Int): Int {
    if (n == 0) return 0
    if (n == 1) return 1
    return _fibonacci(n - 1) + _fibonacci(n - 2)
  }
  return _fibonacci(n)
}


class Stack {

  private class Node(val value: Int) {
    var next: Node? = null
  }

  private var head: Node? = null

  fun push(v: Int) {
    val node = Node(v)
    node.next = head
    head = node
  }

  fun pop(): Int {
    val _head = head ?: throw IllegalStateException("empty stack")
    head = _head.next
    return _head.value
  }
}


class Queue {

  private class Node(val value: Int) {
    var next: Node? = null
  }

  private var head: Node? = null

  fun push(v: Int) {
    val node = Node(v)
    val head = this.head
    if (head == null) {
      this.head = node
      return
    }
    var last: Node = head
    while (last.next != null) last = last.next!!
    last.next = node
  }

  fun poll(): Int {
    val _head = head ?: throw IllegalStateException("empty queue")
    head = _head.next
    return _head.value
  }
}
