#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:55
# @Author  : 黄权权
# @File    : main.py
# @Software: PyCharm
import pytest

from pylib.web_UI_lib.pageObjects.commonPage import CommonPage

if __name__ == '__main__':
    # pytest.main(["-s", "-k test_test.py"])

    c = CommonPage()
    c.move_to_nav_left_location()
    c.test()
