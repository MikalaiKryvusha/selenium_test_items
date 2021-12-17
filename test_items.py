import time
import math
import pytest
from selenium import webdriver


class TestItems:

    def test_items(self, browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        # test flow
        button = False
        css_locator = "button.btn-add-to-basket"
        button = self.wait_for_locator(browser, css_locator, timeout=20)
        time.sleep(3)

        assert button

    def wait_for_locator(self, browser, locator, timeout):

        while True:
            if timeout == 0:
                raise Exception("Timeout!")

            try:
                element = browser.find_element_by_css_selector(locator)
                return True
            except:
                timeout -= 1
                time.sleep(1)
        pass