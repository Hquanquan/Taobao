#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 12:56
# @Author  : 黄权权
# @File    : homePage.py
# @Software: PyCharm
from pylib.web_UI_lib.pageObjects.basePage import BasePage


class HomePage(BasePage):
    """
    首页
    """
    def __init__(self):
        # 继承父类的__init__()构造方法
       super(HomePage, self).__init__()
