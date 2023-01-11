# -*- coding: utf-8 -*-
# コマンドライン引数で「テスト対象の作業ディレクトリ」を渡す
import sys
target_workdir = sys.argv[1]

import os
#「python setup.py /ram」でTrue
if os.path.isdir(target_workdir):
    os.chdir(target_workdir)
else:
    print(f'指定されたパスが見つかりません: {target_workdir}')
    exit(1)

if not os.path.isdir('./temp'):
    print('対象ディレクトリ内に「.hakuchumu」が見つかりません')
    exit(1)