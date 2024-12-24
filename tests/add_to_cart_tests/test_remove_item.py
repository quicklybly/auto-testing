import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRemoveItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_remove_item(self):
        driver = self.driver

        first_product_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]'
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, first_product_xpath)))

        time.sleep(1)

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.1);")

        add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]/div/div/div/div/article/div/div/div/div[3]/button'
        add_to_cart_button = first_product.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        time.sleep(2)

        cart_button_xpath = '//*[@id="__layout"]/div/header/div[2]/div[2]/button[5]'
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, cart_button_xpath)))
        cart_button.click()

        time.sleep(1)

        change_element_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article'
        change_element = self.wait.until(EC.presence_of_element_located((By.XPATH, change_element_xpath)))
        ActionChains(driver).move_to_element(change_element).perform()
        time.sleep(2)

        delete_button_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article/div[2]/div[1]/button'
        delete_button = change_element.find_element(By.XPATH, delete_button_xpath)
        delete_button.click()

        empty_cart_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[1]/article/div/section/h2'
        empty_cart = self.wait.until(EC.presence_of_element_located((By.XPATH, empty_cart_xpath)))

        self.assertEqual(empty_cart.text, 'в корзине\nничего нет...')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
