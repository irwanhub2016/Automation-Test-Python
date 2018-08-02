from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestVodkaTransaksi(unittest.TestCase):
	"""docstring for ClassName"""

#deifini fungsi open driver untuk firefox
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_vodka_transaksi(self):
		driver = self.driver
		driver.get("http://vodka.xwork.co")
		driver.find_element_by_xpath("//button[@id='search-room-submit']/label").click()

		assert "Not Result Found" not in driver.page_source

	def tearDown(self):
		print ('QA - XWORK Success !')
		self.driver.close()


if __name__ == "__main__":
    unittest.main()