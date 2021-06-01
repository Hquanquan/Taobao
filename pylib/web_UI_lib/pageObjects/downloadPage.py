#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 12:56
# @Author  : 黄权权
# @File    : downloadPage.py
# @Software: PyCharm
# @Desc    : 下载页面
from pylib.web_UI_lib.pageObjects.commonPage import CommonPage


class DownloadPage(CommonPage):
    """
    PC下载页
    """
    def __init__(self):
        # 继承父类的__init__()构造方法
        super().__init__()

