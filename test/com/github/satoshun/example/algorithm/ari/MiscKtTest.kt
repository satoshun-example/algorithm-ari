package com.github.satoshun.example.algorithm.ari

import org.hamcrest.CoreMatchers.`is`
import org.junit.Assert.assertThat
import org.junit.Test

class MiscKtTest {

  @Test fun fibonacci1() {
    assertThat(fibonacci(10), `is`(55))
  }

  @Throws(Exception::class)
  @Test(expected = IllegalStateException::class) fun stack_exception() {
    val stack = Stack()
    stack.pop()
  }

  @Throws(Exception::class)
  @Test fun stack_success() {
    val stack = Stack()
    stack.push(100)
    assertThat(stack.pop(), `is`(100))

    stack.push(200)
    stack.push(300)
    stack.push(400)
    assertThat(stack.pop(), `is`(400))
    assertThat(stack.pop(), `is`(300))
    assertThat(stack.pop(), `is`(200))
  }

  @Throws(Exception::class)
  @Test fun queue_success() {
    val queue = Queue()
    queue.push(100)
    assertThat(queue.poll(), `is`(100))

    queue.push(200)
    queue.push(300)
    queue.push(400)
    queue.push(500)
    assertThat(queue.poll(), `is`(200))
    assertThat(queue.poll(), `is`(300))
    assertThat(queue.poll(), `is`(400))
    assertThat(queue.poll(), `is`(500))
  }
}
