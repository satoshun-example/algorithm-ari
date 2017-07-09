package com.github.satoshun.example.algorithm.ari.two

import com.google.common.truth.Truth
import org.junit.Test

class PoolSearchKtTest {
  @Test fun _poolSearch() {
    Truth.assertThat(poolSearch(
        listOf(
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
            0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ),
        12,
        3
    )).isEqualTo(2)
  }

  @Test fun __poolSearch() {
    Truth.assertThat(poolSearch(
        listOf(
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
            0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0
        ),
        12,
        5
    )).isEqualTo(5)
  }
}