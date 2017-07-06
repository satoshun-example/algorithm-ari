package com.github.satoshun.example.algorithm.ari


fun triangle(candidates: List<Int>): Int? {
  var max: Int = 0
  (0 until candidates.size - 2).forEach { i ->
    (i + 1 until candidates.size - 1).forEach { j ->
      (j + 1 until candidates.size).forEach { k ->
        val v1 = candidates[i]
        val v2 = candidates[j]
        val v3 = candidates[k]
        val a = getTriangleValue(v1, v2, v3)
            ?: getTriangleValue(v2, v1, v3)
            ?: getTriangleValue(v3, v2, v1)
        if (a != null && a > max) max = a
      }
    }
  }
  return if (max == 0) null else max
}

private fun getTriangleValue(v1: Int, v2: Int, v3: Int): Int? =
    if (v1 >= v2 && v1 >= v3) {
      if (v2 + v3 > v1)
        v1 + v2 + v3 else
        null
    } else null
