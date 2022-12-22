# -*- coding: utf-8 -*-

#このファイル単体でもセッタは生成できる

file = open('setter_code.py', 'w', encoding='utf8')

def append_setter(file, id: str):
    file.write(f"\telif id == '{id}':\n")
    file.write(f"\t\telement = driver.find_element(By.ID, id)\n")
    file.write(f"\t\telement.send_keys(value)\n")
    return

def create_setter_code_file(id_list: list[str]):
    #file = open('setter_code.py', 'w', encoding='utf8')
    file.write("# -*- coding: utf-8 -*-\n")
    file.write("# このファイルはcreate_setter_code.pyによって生成されました\n")
    file.write("#でも結局このファイルは1回しか生成しないし、人間の行動(入力に限らず)リストを生成した方が良いような気がするんだよなぁ\n\n")
    file.write("from selenium.webdriver.common.by import By\n")
    file.write("\n")
    file.write("def setter(driver, id, value):\n")
    file.write("\tif id == '':\n")
    file.write("\t\tpass\n")
    for id in id_list:
        append_setter(file, id)
    #file.close()
    return

create_setter_code_file(['hoge', 'fuge', 'hage'])
# セッタ出力完了

# 以下、行動のリスト生成
file.write("\nfrom driver import get_driver\ndriver = get_driver()\n# 今はそれぞれのidに対してそれぞれの値を代入するだけ\n")
for id in ['hoge', 'fuge', 'hage']:
    for value in ['a','b','c','d']:
        file.write(f"setter(driver, '{id}', '{value}')\n")
file.write("driver.close()\n")
file.close()
print('「setter_code.py」生成完了')