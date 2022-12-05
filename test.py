# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定

driver = webdriver.Chrome(options=options)
driver.get('file:///' + os.getcwd() + '/index.html')

from setter import create_setter
setter = create_setter('id11', driver)





# type毎に代表的な値を代入してみる
# 実際に使うときはidと値のjsonファイルで作成する
import codecs
import json
def create_case(setter, value):
    f = codecs.open('sampleValue.json', 'r', "utf8")
    # 各言語毎のプロパティファイルをここで辞書型でロードしておく
    json_dict = json.load(f)
    print(json_dict['number'])
    # setter(value)
    setter(json_dict['number'][1])
    return
create_case(setter, "")

sleep(5)
driver.close()