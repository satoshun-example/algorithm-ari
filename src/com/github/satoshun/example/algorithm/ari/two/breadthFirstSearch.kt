package com.github.satoshun.example.algorithm.ari.two

private fun move(x: Int, start: Int, maps: List<Char>, records: MutableList<Int>): Boolean {
  val step = records[start]

  fun _move(pos: Int): Boolean {
    if (maps[pos] == 'G') {
      return true
    }
    if (maps[pos] == '.' && records[pos] == -2) {
      records[pos] = step + 1
    }
    return false
  }

  records[start] = -3
  // move top
  if (start > x) {
    if (_move(start - x)) return true
  }
  // move left
  if (start % x != 0) {
    if (_move(start - 1)) return true
  }
  // move right
  if (start % x != x - 1) {
    if (_move(start + 1)) return true
  }
  // move bottom
  if (start + x < maps.size) {
    if (_move(start + x)) return true
  }

  return false
}

fun breadthFirstSearch(maps: List<Char>, x: Int): Int {
  val start = maps.indexOf('S')
  val records = MutableList(maps.size, { -2 })
  records[start] = 0
  var steps = 0
  while (true) {
    val i = records.indexOf(steps)
    if (i == -1) {
      steps++
      continue
    }
    if (move(x, i, maps, records)) {
      break
    }
  }
  return ++steps
}
