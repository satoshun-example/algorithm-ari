package com.github.satoshun.example.algorithm.ari

import org.hamcrest.CoreMatchers
import org.hamcrest.core.IsNull.nullValue
import org.junit.Assert.assertThat
import org.junit.Test

class TriangleKtTest {

  @Test fun triangle_() {
    val result = triangle(
        listOf(2, 5, 10, 4)
    )
    assertThat(result, CoreMatchers.`is`(11))
  }

  @Test fun triangle__() {
    val result = triangle(
        listOf(2, 5, 10, 3)
    )
    assertThat(result, nullValue())
  }

  @Test fun triangle___() {
    val result = triangle(
        listOf(2, 5, 10, 4, 3)
    )
    assertThat(result, CoreMatchers.`is`(12))
  }
}
