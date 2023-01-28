# -*- coding: utf-8 -*-

#このファイル単体でもセッタは生成できる

file = open('setter_code.py', 'w', encoding='utf8')

def append_setter(file, id: str):
    file.write(f"\telif id == '{id}':\n")
    file.write(f"\t\telement = driver.find_element(By.ID, id)\n")
    file.write(f"\t\telement.send_keys(value)\n")
    return

def create_setter_code_file():
    file = open('setter_code.py', 'w', encoding='utf8')
    file.write("# -*- coding: utf-8 -*-\n")
    file.write("# このファイルはcreate_setter_code.pyによって生成されました\n")
    file.write("#でも結局このファイルは1回しか生成しないし、人間の行動(入力に限らず)リストを生成した方が良いような気がするんだよなぁ\n\n")
    file.write("from selenium.webdriver.common.by import By\n")
    file.write("\n")
    file.write("def setter(driver, id, value):\n")
    file.write("\tif id == '':\n")
    file.write("\t\tpass\n")
    file.write("\telse:\n")
    file.write("\t\telement = driver.find_element(By.ID, id)\n")
    file.write("\t\telement.send_keys(value)\n")
    # for id in id_list:
    #     append_setter(file, id)
    #file.close()
    return

def create_setter_code_per_url(url: str):
    print(url + 'に対してのセッタコードを出力します')
    create_setter_code_file()
    return