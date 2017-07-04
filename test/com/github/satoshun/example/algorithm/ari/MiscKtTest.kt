package com.github.satoshun.example.algorithm.ari

import org.hamcrest.CoreMatchers.`is`
import org.junit.Assert.*
import org.junit.Test

class MiscKtTest {

  @Test fun fibonacci1() {
    assertThat(fibonacci(10), `is`(55))
  }
}