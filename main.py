# -*- coding: utf-8 -*-
# 事前にやっておくこと
# 1.chromedriver.exe
# 2.pip install chromedriver-binary

import random
import os
import codecs
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

outputfile_name = 'output.txt'

# os.remove(outputfile_name)

# 今はファイルに追記モードで書き出しているが後々はDBに書き出す
file = codecs.open(outputfile_name, 'w', "utf8")
# for i in range(5):
#     file.write(str(i) + '\n')

def out(output_string):
    #print(output_string)
    file.write(output_string + '\n')

# inputに対して入力するセッタを作成
def create_setter(id):
    def setter(value):
        print(id + "に" + value+"をセットします")
        return
    return setter

options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
driver = webdriver.Chrome(options=options)
driver.get('file:///' + os.getcwd() + '/index.html')

# 基本は DFS で掘っていく
# 観察対象のゲッタのリストを(DBのカラムと画面の入力項目)
def capture():
    input_elements = driver.find_elements(By.TAG_NAME, "input")
    return [i.get_attribute('value') for i in input_elements]

input_elements = driver.find_elements(By.TAG_NAME, "input")
for i in input_elements:
    input_type = i.get_attribute("type")
    # idはなくても入力できるがログに出力できないためidは必須か
    out(f'id="{i.get_attribute("id")}" type="{input_type}"')
    out(f'id="{i.get_attribute("id")}" type="{input_type}"')
    if input_type == 'hidden' or input_type == 'file':
        continue
    # ランダムな値を入力
    input_value = random.randint(5, 10)
    i.send_keys(input_value)
    #print(capture())

file.close()
file = codecs.open(outputfile_name, 'r', "utf8")
for i in file.readlines():
    print(i.strip())
driver.quit()

