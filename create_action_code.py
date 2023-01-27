# -*- coding: utf-8 -*-

def create_action_code_per_url(url: str):
    print(url + 'に対してのアクションコードを出力します')
    file = open('action_code.py', 'w', encoding='utf8')
    file.write("import os\n")
    file.write("\nfrom driver import get_driver\ndriver = get_driver()\n# 今はそれぞれのidに対してそれぞれの値を代入するだけ\n")
    file.write("driver.get('file:///' + os.getcwd() + '/index.html')\n")
    # from sample_value_for_id import get_sample_value_dict_for_id
    # x = get_sample_value_dict_for_id()
    # for id, value_list in x.items():
    #     if value_list == None:
    #         continue
    #     for value in value_list:
    #         file.write(f"setter(driver, '{id}', '{value}')\n")
    #         file.write(f"import time\ntime.sleep(0.5)\n")
    # file.write("driver.close()\n")
    file.close()