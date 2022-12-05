# -*- coding: utf-8 -*-
# これで問題はこのファイルの中身を自動生成すればOKということに

from selenium.webdriver.common.by import By

# セッタを返す
def create_setter(id, driver):
    def setter(value):
        input_element = driver.find_element(By.ID, id)
        input_element.send_keys(value)
        return
    return setter

# どうしても入力作業は人間が書かなければならない。
# なぜか入力できないときもあるので。
# つまりcreate_setter関数はページ毎に手動で書かないといけない。
# じゃ、どこを自動で書くかといううと
# 出力はDBに丸投げるので