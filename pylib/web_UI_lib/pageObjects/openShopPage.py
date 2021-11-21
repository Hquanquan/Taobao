#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 22:49
# @Author  : 黄权权
# @File    : openShopPage.py
# @Software: PyCharm
# @Desc    : 新商家开店页
from pylib.web_UI_lib.pageObjects.basePage import BasePage


class OpenShopPage(BasePage):
    """
    新商家开店页
    """
    def __init__(self):
        # 继承父类的__init__()构造方法
        super(OpenShopPage, self).__init__()
