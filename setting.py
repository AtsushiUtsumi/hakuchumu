# -*- coding: utf-8 -*-
class Settings:
    # コンストラクタにディレクトリを取って各変数を初回化するようにする
    url_list = [""]
    hakuchum_dir = ''
    @staticmethod
    def get_urls():
        return Settings.url_list
    def get_hakuchum_dir():
        return Settings.hakuchum_dir

def get_setting():
    settings = dict()
    settings[''] = ''
    return settings