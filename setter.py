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




# 出力したいコードをイメージ出来ているのか
def append_setter(file, test_case):
    file.write("print('これはテストコードです')")
    return

def create_test_code_file(input_sequence, check_output):
    file = open('auto.py', 'w', encoding='utf8')
    file.write("# -*- coding: utf-8 -*-\n")
    append_setter(file, None)
    file.close()
    return

create_test_code_file('', '')

import auto#これで実行はあまりにダサいがひとまずこれで...

# 実行コード実行結果からテストコードを生成するのが目的では?
# なので仮にサーバサイド未実装でhtmlだけのアプリがあった場合
# でもhakuchumuは動作しなければならないハズ
# もちろんその場合hakuchumuとしては「何の動作もしない」という事を出力しなければならない
# 現時点でhakuchumu自体のテストにはhtmlのみでOKといううことになる

# セッタに関しては人力が必要になるとは思うが、それでも自動生成機能は有った方が良い