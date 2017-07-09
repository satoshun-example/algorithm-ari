package com.github.satoshun.example.algorithm.ari.two

private fun depthFirstSearch(candidates: List<Int>, k: Int, value: Int, depth: Int): Boolean {
  if (value == k) {
    return true
  }
  if (depth == candidates.size) {
    return false
  }
  return depthFirstSearch(candidates, k, value + candidates[depth], depth + 1)
      || depthFirstSearch(candidates, k, value, depth + 1)
}

fun depthFirstSearch(candidates: List<Int>, k: Int): Boolean {
  return depthFirstSearch(candidates, k, 0, 0)
}
