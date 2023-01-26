# -*- coding: utf-8 -*-
from settings import settings
import os

class Route:
    url = ''
    url_dir = ''
    def __init__(self, url:str):
        self.url_dir = settings.hakuchumu_dir
        self.url = url
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
        print(self.url + '')
        return
    
    def create_action_code(self):
        self.chdir_url_dir()
        print(self.url + '')
        return