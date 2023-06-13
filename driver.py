# -*- coding: utf-8 -*-

# ドライバの取得方法は頻繁に変わるのでここで関数化しておく

from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options


def get_driver():
    try:
        # TODO: 環境変数から取得するように変更する
        CHROMEDRIVER = './chromedriver'
        options = Options()
        # ヘッドレスで起動するオプションを指定
        # options.headless = True
        # 不要なエラーを非表示
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        chrome_service = fs.Service(executable_path=CHROMEDRIVER)
        driver = webdriver.Chrome(service=chrome_service, options=options)
        return driver
    except:
        print('ドライバエラー')
        exit(0)
