# -*- coding: utf-8 -*-
import os
# urlはディレクトリ名にできないのでURL辞書型で紐づける形式にしておく
# url毎にIDを振った辞書型のコードを作成する
def footprint(id: int, url: str):
    os.mkdir(str(id))
    os.chdir(str(id))
    f = open('id.txt', 'w')
    f.write(url)
    f.close()
    os.chdir('..')
    return

def create_code_per_url():
    hakuchumu_dir = './.hakuchumu'
    os.chdir(hakuchumu_dir)
    url_file = open('url_list.txt', 'r')
    url_list_py = open('url_list.py', 'w')
    url_list_py.write('# create_action_code.pyから自動生成\n')
    url_list_py.write('url_dict = dict()\n')
    id = 0
    for url in [i.strip('\n') for i in url_file.readlines()]:
        id += 1

        # ひとまずそのURLの設定ファイルであると分かるようにしておく
        footprint(id, url)


        url_list_py.write(f'url_dict[\'{url}\'] = {id}\n')
    url_list_py.write('print(url_dict)\n')
    url_list_py.close()
    return

# 動作確確認
create_code_per_url()
