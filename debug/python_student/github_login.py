# -*- coding: utf-8 -*-
"""
@author     :Pineapple

@Blog       :https://blog.csdn.net/pineapple_C

@contact    :cppjavapython@foxmail.com

@time       :2020/8/19 8:50

@file       :github.py

@desc       :
"""
from pyquery.pyquery import PyQuery as pq
from requests.packages import urllib3
import requests


class Github:
    def __init__(self):
        """
        初始化

        """
        urllib3.disable_warnings()
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        # 个人主页
        self.self_url = 'https://github.com/Pineapple666'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.session = requests.Session()

    def login(self, username, password):
        """
        提交表单，登录

        :param username: 用户名
        :param password: 密码
        :return: None
        """
        post_data = {
            'webauthn-iuvpaa-support': 'supported',
            'authenticity_token': self.token(),
            'webauthn-support': 'supported',
            'required_field_b538': None,
            'password': password,
            'commit': 'Sign in',
            'login': username,
            'return_to': None,
        }
        response = self.session.post(url=self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print('login in successful!')
        else:
            print(f'response status code = {response.status_code}')

    def token(self):
        """
        获取authenticity_token字段信息

        :return: None
        """
        response = self.session.get(url=self.login_url, headers=self.headers, verify=False)
        if response.status_code == 200:
            html = response.text
            doc = pq(html)
            print(doc)
            return doc('input[name="authenticity_token"]').attr('value')
        else:
            print(f'response status code = {response.status_code}')

    def test(self):
        """
        测试登录成功，输出用户ID

        :return: None
        """
        response = self.session.get(url=self.self_url, headers=self.headers, verify=False)
        if response.status_code == 200:
            html = response.text
            doc = pq(html)
            id = doc('span[itemprop="additionalName"]').text()
            print(f'your id is {id}')
        else:
            print(f'response status code = {response.status_code}')

        a = "Y_YVqpyMecnL-NlaGvk4Jfg74zn6fN8Ypb6rz88-Jfqg-kiM"
        b = "DZ1T2_-2VXBeJZGh2TmWLkhYynXMh8kciC-uKVV_VgRlBlh_"


if __name__ == '__main__':
    github = Github()
    github.login("daixiang11", "Dx3826729")
    a = github.token()
    print(a)
    github.test()
