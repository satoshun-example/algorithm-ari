package com.github.satoshun.example.algorithm.ari

import org.hamcrest.CoreMatchers.`is`
import org.junit.Assert.assertThat
import org.junit.Test

class AntsBruteForceKtTest {

  @Test fun antBruteForce__() {
    val result = antBruteForce(
        listOf(2),
        10
    )
    assertThat(result.min, `is`(2))
    assertThat(result.max, `is`(8))
  }

  @Test fun antBruteForce_() {
    val result = antBruteForce(
        listOf(2, 4, 8, 5),
        10
    )
    assertThat(result.min, `is`(5))
    assertThat(result.max, `is`(8))
  }
}

class AntsKtTest {

  @Test fun ant__() {
    val result = ant(
        listOf(2),
        10
    )
    assertThat(result.min, `is`(2))
    assertThat(result.max, `is`(8))
  }

  @Test fun ant_() {
    val result = ant(
        listOf(2, 4, 8, 5),
        10
    )
    assertThat(result.min, `is`(5))
    assertThat(result.max, `is`(8))
  }
}
