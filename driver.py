# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options

def get_driver():
    CHROMEDRIVER = './chromedriver'
    options = Options()

    # ヘッドレスで起動するオプションを指定
    # options.headless = True

    chrome_service = fs.Service(executable_path=CHROMEDRIVER)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver
