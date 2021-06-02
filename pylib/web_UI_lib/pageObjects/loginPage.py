#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:15
# @Author  : 黄权权
# @File    : loginPage.py
# @Software: PyCharm
# @Desc    : 淘宝网站登录页面
from pylib.web_UI_lib.pageObjects.basePage import BasePage


class LoginPage(BasePage):
    """
    淘宝网站登录页面,
    1、页面元素
    2、相关页面元素的方法
    """

    def __init__(self):
        # 继承父类的__init__()构造方法
        # super().__init__()
        super(LoginPage, self).__init__()

        # 密码登录文案
        self.login_text = ['xpath', '//*[@id="login"]/div[2]/div/div[1]/a[1]']

    def get_login_text(self):
        """
        获取登录页面中，密码登录文案
        :return:
        """
        return self.get_element_text(self.login_text)
