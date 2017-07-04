package com.github.satoshun.example.algorithm.ari

fun fibonacci(n: Int): Int {
  fun _fibonacci(n: Int): Int {
    if (n == 0) return 0
    if (n == 1) return 1
    return _fibonacci(n - 1) + _fibonacci(n - 2)
  }
  return _fibonacci(n)
}
