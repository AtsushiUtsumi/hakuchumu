# -*- coding: utf-8 -*-
import json
import codecs
filename = "sampleValue.json"

json_file = codecs.open(filename, 'r', "utf8")
# 各言語毎のプロパティファイルをここで辞書型でロードしておく
test = json.load(json_file)
# print(test)
# for i, key in enumerate(test.keys()):
#     print(str(i) + ":" + key)

def get_sample_value_for_type(type: str):
    if type in test.keys():
        return test[type]
    else:
        return None