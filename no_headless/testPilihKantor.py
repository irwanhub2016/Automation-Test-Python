# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestVodkaTransaksi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_vodka_transaksi(self):
        print "Choosing Office ... \n" 
        driver = self.driver
        driver.get("http://vodka.xwork.co")
        driver.find_element_by_xpath("//div[@id='headerTitleContainer']/div/div/div/div[2]").click()
        driver.find_element_by_id("search-room-input-query").click()
        driver.find_element_by_xpath("//div[@id='headerTitleContainer']/div/div/div[2]/div/div[2]/ul/li[5]/div").click()
        driver.find_element_by_xpath("//div[@id='headerTitleContainer']/div/div/div[2]/div[2]/div/button/span").click()
        driver.find_element_by_link_text("Diatas 20").click()
        Select(driver.find_element_by_id("filterCapacity")).select_by_visible_text("Diatas 20")
        driver.find_element_by_xpath("//div[@id='priceSlider']/div[6]").click()
        driver.find_element_by_id("priceSlider").click()
        driver.find_element_by_xpath("//div[@id='headerTitleContainer']/div/div/div[2]/div[2]").click()
        driver.find_element_by_xpath("//div[@id='priceSlider']/div[6]").click()
        driver.find_element_by_xpath("//div[@id='headerTitleContainer']/div/div/div[2]/div[2]").click()
        driver.find_element_by_xpath("//div[@id='priceSlider']/div[5]").click()
        driver.find_element_by_id("search-room-submit").click()
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[2]/div/div/div/div[3]/div/div/text").click()

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
        time.sleep(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "Testing for Pilih Kantor is Success"

if __name__ == "__main__":
    unittest.main()