# -*- coding: utf-8 -*-
import os
import json
from sample_value_for_type import get_sample_value_for_type
from driver import get_driver

driver = get_driver()

target_url = 'file:///' + os.getcwd() + '/index.html'

driver.get(target_url)
import codecs
from selenium.webdriver.common.by import By

outputfile_name = 'sampleValueForId.json.sample'
file = codecs.open(outputfile_name, 'w', "utf8")
input_elements = driver.find_elements(By.TAG_NAME, "input")


dict = dict()
for i in input_elements:
    id = i.get_attribute("id")
    input_type = i.get_attribute("type")
    print(input_type)
    dict[id] = get_sample_value_for_type(input_type)
driver.quit()
# htmlのid毎の入力値のサンプルをjsonで生成
with open("sample.json", "w") as outfile:
    json.dump(dict, outfile, indent=4)

def get_sample_value_dict_for_id():
    return dict

def get_sample_value_for_id(id):
    return dict[id]