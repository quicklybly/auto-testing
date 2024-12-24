import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToCartMultiple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_add_multiple_products_to_cart(self):
        driver = self.driver

        first_product_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]'
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, first_product_xpath)))

        second_product_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[2]'
        second_product = self.wait.until(EC.presence_of_element_located((By.XPATH, second_product_xpath)))

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")

        add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]/div/div/div/div/article/div/div/div/div[3]/button'
        add_to_cart_button = first_product.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[2]/div/div/div/div/article/div/div/div/div[3]/button'
        add_to_cart_button = second_product.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        time.sleep(2)

        cart_button_xpath = '//*[@id="__layout"]/div/header/div[2]/div[2]/button[5]'
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, cart_button_xpath)))
        cart_button.click()

        cart_items_container_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div'
        cart_items_container = self.wait.until(EC.presence_of_element_located((By.XPATH, cart_items_container_xpath)))

        child_elements = cart_items_container.find_elements(By.XPATH, './*')
        child_count = len(child_elements)

        self.assertEquals(
            child_count,
            2,
            "FAILED: expected cart size: '2'",
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
