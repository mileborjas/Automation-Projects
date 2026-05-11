# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC01EcommercePurchaseLoop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c01_ecommerce_purchase_loop(self):
        driver = self.driver
                driver.get("https://automationexercise.com/")
                driver.find_element_by_link_text(u" Products").click()
                driver.find_element_by_id("search_product").click()
                productName = "TSHIRT"
                driver.find_element_by_id("search_product").clear()
                driver.find_element_by_id("search_product").send_keys(productName)
                driver.find_element_by_id("submit_search").click()
                self.is_element_present(By.LINK_TEXT, "View Product")
                driver.find_element_by_link_text("View Product").click()
                driver.find_element_by_xpath("//button[@type='button']").click()
                driver.find_element_by_xpath("//div[@id='cartModal']/div/div/div[3]/button").click()
                try: self.assertEqual("Your product has been added to cart.", driver.find_element_by_xpath("//*[@id=\"cartModal\"]/div/div/div[2]/p[1]").text)
                except AssertionError as e: self.verificationErrors.append(str(e))
                counter = "0"
                while counter < 3 :
                    driver.find_element_by_xpath("//button[@type='button']").click()
                    driver.find_element_by_xpath("//div[@id='cartModal']/div/div/div[3]/button").click()
                    counter = driver.execute_script("return Number(" + str(counter) + ") + 1")
                    #ERROR: Caught exception [ERROR: Unsupported command [gotoIf | ${counter} < 3 | inicio_bucle]]
                    try: self.assertEqual("Your product has been added to cart.", driver.find_element_by_xpath("//*[@id=\"cartModal\"]/div/div/div[2]/p[1]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
