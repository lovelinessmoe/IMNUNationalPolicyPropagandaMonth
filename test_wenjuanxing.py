# coding=utf-8

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Page.imnu import imnu


class TestDemo:

    def setup_class(self):
        self.url = "https://ks.wjx.top/vm/P8rupiz.aspx"
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--lang=zh-CN")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        self.ddp = imnu(self.driver, self.url)

    def test_shop(self):
        name = ""
        school = "计算机科学与技术学院"
        num = ""
        self.ddp.test_imnu(name, school, num)


if __name__ == '__main__':
    pytest.main()
