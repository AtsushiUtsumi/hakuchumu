# -*- coding: utf-8 -*-
import os

# クラス変数で設定するのかインスタンス変数でするのかを決める
class Settings:
    # ユーザーの設定はhakuchumu本体のディレクトリから参照する
    hakuchumu_dir_user: str = os.getcwd()
    # TODO: 引数から初期化する
    hakuchumu_dir_workspace: str = os.getcwd() + '/.hakuchumu'
    def __init__(self, hakuchumu_dir_workspace: str):
        Settings.hakuchumu_dir_workspace = hakuchumu_dir_workspace
        return