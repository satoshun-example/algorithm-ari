package com.github.satoshun.example.algorithm.ari.two

import com.google.common.truth.Truth
import org.junit.Test

class BreadthFirstSearchKtTest {
  @Test fun _breadthFirstSearch() {
    Truth.assertThat(breadthFirstSearch(
        listOf(
            '#', 'S', '#', '#', '#', '#', '#', '#', '.', '#',
            '.', '.', '.', '.', '.', '.', '#', '.', '.', '#',
            '.', '#', '.', '#', '#', '.', '#', '#', '.', '#',
            '.', '#', '.', '.', '.', '.', '.', '.', '.', '.',
            '#', '#', '.', '#', '#', '.', '#', '#', '#', '#',
            '.', '.', '.', '.', '#', '.', '.', '.', '.', '#',
            '.', '#', '#', '#', '#', '#', '#', '#', '.', '#',
            '.', '.', '.', '.', '#', '.', '.', '.', '.', '.',
            '.', '#', '#', '#', '#', '.', '#', '#', '#', '.',
            '.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'
        ),
        10
    )).isEqualTo(22)
  }
}
