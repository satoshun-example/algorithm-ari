package com.github.satoshun.example.algorithm.ari.two

private fun fillMaps(maps: MutableList<Int>, start: Int, x: Int, y: Int) {
  maps[start] = 0
  val left = (start % x == 0)
  val right = (start % x == x - 1)
  val top = (start in 0..x - 1)
  val bottom = (start in maps.size - x..maps.size)
  if (!left && !top && maps[start - 1 - x] == 1) fillMaps(maps, start - 2 - x, x, y)
  if (!top && maps[start - x] == 1) fillMaps(maps, start - 1 - x, x, y)
  if (!top && !right && maps[start + 1 - x] == 1) fillMaps(maps, start + 1 - x, x, y)
  if (!left && maps[start - 1] == 1) fillMaps(maps, start - 1, x, y)
  if (!right && maps[start + 1] == 1) fillMaps(maps, start + 1, x, y)
  if (!left && !bottom && maps[start - 1 + x] == 1) fillMaps(maps, start - 1 + x, x, y)
  if (!bottom && maps[start + x] == 1) fillMaps(maps, start + x, x, y)
  if (!right && !bottom && maps[start + 1 + x] == 1) fillMaps(maps, start + 1 + x, x, y)
}

/**
 * Lake Counting
 */
fun poolSearch(_maps: List<Int>, x: Int, y: Int): Int {
  val maps = _maps.toMutableList()
  var a = 0
  for (i in maps.indices) {
    if (maps[i] == 0) continue
    fillMaps(maps, i, x, y)
    a += 1
  }
  return a
}
