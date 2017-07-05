package com.github.satoshun.example.algorithm.ari

data class AntPair(val min: Int, val max: Int)

fun antBruteForce(pos: List<Int>, len: Int): AntPair {
  var max = Integer.MIN_VALUE
  var min = Integer.MAX_VALUE
  for (i in 0..pos.size.pow(2) - 1) {
    var dm = 0
    pos.forEachIndexed { index, v ->
      val d = if ((i and index.pow(2)) == 0) v else len - v
      if (d > dm) dm = d
    }
    if (dm > max) max = dm
    if (dm < min) min = dm
  }
  return AntPair(min, max)
}

fun ant(pos: List<Int>, len: Int): AntPair {
  var max = Integer.MIN_VALUE
  var min = Integer.MIN_VALUE
  for (p in pos) {
    val (maxP, minP) = if (len - p > p)
      Pair(len - p, p) else
      Pair(p, len - p)
    if (maxP > max) max = maxP
    if (minP > min) min = minP
  }
  return AntPair(min, max)
}

private fun Int.pow(n: Int): Int {
  // same Math.pow
  return (1..this).fold(1) { acc, _ -> acc * n }
}
