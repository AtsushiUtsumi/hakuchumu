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

# URLからディレクトリのパスを返す(無ければ作成する)
def get_dir_by_url(url: str) -> str:
    id = 1
    while os.path.isdir(f'{id}'):
        id += 1
    dir = str(id)
    os.mkdir(dir)
    return dir


from create_setter_code import create_setter_code_per_url
from create_action_code import create_action_code_per_url
# 与えられたURL用の出力ディレクトリを作成、中にそのURL内で有効なセッタ、アクションを「.py」で出力する
def create_code_per_url(url: str):
    dir = get_dir_by_url(url)
    print('[' + dir + ']に対してのコード生成')
    os.chdir(dir)
    url_file = open('url.txt', 'w')
    url_file.write(url)
    # セッタファイル生成処理
    create_setter_code_per_url(url)
    # アクションファイル生成処理
    create_action_code_per_url(url)
    os.chdir('..')#hakushuホームに戻るのが良いかも
    return

# urlリストの中の全てのURLに対して処理を実行
def create_code_all_url():
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
create_code_per_url('https://github.com/AtsushiUtsumi?tab=repositories')



def hoge():
    print('import出来た' + os.getcwd())