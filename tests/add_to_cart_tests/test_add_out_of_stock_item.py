import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddOutOfStockItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/19000165312-versense")
        self.wait = WebDriverWait(self.driver, 10)
        self.add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/article/div[1]/div[1]/form/div[4]/div/button'

    def test_add_ended_product_to_cart_from_product(self):
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((
            By.XPATH, self.add_to_cart_button_xpath
        )))

        self.assertEqual(
            add_to_cart_button.text,
            'УЗНАТЬ О ПОСТУПЛЕНИИ',
            "Test failed: Item is absent from cart.",
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
