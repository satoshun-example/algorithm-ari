package com.github.satoshun.example.algorithm.ari.two

import com.google.common.truth.Truth
import org.junit.Test

class DepthFirstSearchKtTest {

  @Test fun _depthFirstSearch() {
    Truth
        .assertThat(depthFirstSearch(listOf(1, 2, 4, 7), 13))
        .isTrue()
  }

  @Test fun __depthFirstSearch() {
    Truth
        .assertThat(depthFirstSearch(listOf(1, 2, 4, 7), 15))
        .isFalse()
  }
}
