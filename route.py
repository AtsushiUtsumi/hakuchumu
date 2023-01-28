# -*- coding: utf-8 -*-
from settings import Settings
from create_action_code import create_action_code_per_url
from create_setter_code import create_setter_code_per_url
import os
class Route:
    url = ''
    url_dir = ''
    
    # URLからディレクトリのパスを返す(無ければ作成する)
    def get_dir_by_url(url: str) -> str:

        id = 1
        while os.path.isdir(f'{id}'):
            id += 1
        dir = str(id)
        os.mkdir(dir)
        return dir
    
    def __init__(self, url:str):
        self.url = url
        os.chdir(Settings.hakuchumu_dir)
        id = 1
        while os.path.isdir(f'{id}'):
            id += 1
        os.mkdir(str(id))
        self.url_dir = Settings.hakuchumu_dir +'/'+ str(id)
        return
    
    def show(self):
        print('Target url is ' + self.url)
        print('Target url_dir is ' + self.url_dir)
        return
    
    def chdir_url_dir(self):
        os.chdir(self.url_dir)
        return
    
    def create_setter_code(self):
        self.chdir_url_dir()
        create_setter_code_per_url(self.url)
        print(self.url + '')
        return
    
    def create_action_code(self):
        self.chdir_url_dir()
        print(self.url + '')
        create_action_code_per_url(self.url)
        return

route = Route('HOGEHOGE')
route.create_setter_code()
route.create_action_code()
