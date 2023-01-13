# -*- coding: utf-8 -*-
# コマンドライン引数で「テスト対象の作業ディレクトリ」を渡す
import sys
target_workdir = './'
if len(sys.argv) != 2:
    print('作業ディレクトリが入力されていません')
else:
    target_workdir = sys.argv[1]

import os
#「python setup.py /ram」でTrue
if not os.path.isdir(target_workdir):
    print(f'指定されたパスが見つかりません: {target_workdir}')
    exit(1)

os.chdir(target_workdir)
if not os.path.isdir('.hakuchumu'):
    print('対象ディレクトリ内に「.hakuchumu」が見つかりません')
    os.mkdir('.hakuchumu')
os.chdir('.hakuchumu')

# テスト対象の設定フィルダに入っていて欲しいもの
f = open('workdir_setting.txt', 'w')
f.close()
f = open('url_list.txt', 'w')
f.close()