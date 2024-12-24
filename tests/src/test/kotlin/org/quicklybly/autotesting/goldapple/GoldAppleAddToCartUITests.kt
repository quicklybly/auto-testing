package org.quicklybly.autotesting.goldapple

import com.codeborne.selenide.Browsers
import com.codeborne.selenide.Condition.enabled
import com.codeborne.selenide.Condition.visible
import com.codeborne.selenide.Configuration
import com.codeborne.selenide.Selenide.*
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.Test
import kotlin.test.assertTrue

internal class AddToCartUITests {
    companion object {
        @JvmStatic
        @BeforeAll
        fun setUp() {
            Configuration.baseUrl = "https://goldapple.ru"
            Configuration.browser = Browsers.CHROME
            Configuration.timeout = 100_000 // 10s
        }
    }

    @AfterEach
    fun tearDown() {
        closeWebDriver()
    }

    @Test
    fun `test 1`() {
        val productXPath = "//*[@id=\"__layout\"]/div/main/section[3]/div/section/div/div[2]/div[1]"
        val addToCartButtonXPath = "/div/div/div/div/article/div/div/div/div[3]/button"
        val cartButtonXPath = "//*[@id=\"__layout\"]/div/header/div[2]/div[2]/button[5]"
        val cartItemXPath =
            "//*[@id=\"__layout\"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div[1]"

        open("/")

        val product = `$x`(productXPath).shouldBe(visible)

        product.`$x`(addToCartButtonXPath)
            .shouldBe(visible, enabled)
            .click()

        `$x`(cartButtonXPath)
            .shouldBe(visible, enabled)
            .click()

        val cartItem = `$x`(cartItemXPath).shouldBe(visible)

        assertTrue(cartItem.exists(), "Test failed: Item not in cart")
    }

    @Test
    fun `test test`() {
        open("/")

        val newsSection = `$`("section[data-scroll-id='51598048-389a-4ff7-8144-c85e0098afee']")
        newsSection.scrollTo().shouldBe(visible)

//        val product = `$x`(productXPath).shouldBe(visible)
//
//        product.`$x`(addToCartButtonXPath)
//            .shouldBe(visible, enabled)
//            .click()
//
//        `$x`(cartButtonXPath)
//            .shouldBe(visible, enabled)
//            .click()
//
//        val cartItem = `$x`(cartItemXPath).shouldBe(visible)

//        assertTrue(cartItem.exists(), "Test failed: Item not in cart")
    }
}
