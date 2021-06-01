#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 22:35
# @Author  : 黄权权
# @File    : marketPage.py
# @Software: PyCharm
# @Desc    : 淘宝商品分类市场页面
from pylib.web_UI_lib.pageObjects.commonPage import CommonPage


class MarketPage(CommonPage):
    """
    淘宝商品分类市场页面
    """
    def __init__(self):
        # 继承父类的__init__()构造方法
        super().__init__()

